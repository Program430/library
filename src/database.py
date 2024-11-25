import os
import json
import uuid

from typing import List
from dataclasses import fields

FILE = "resourses/data.json"

class DataBaseManager:
    @staticmethod
    def json_to_python(file=FILE) -> List:
        if os.path.exists(file):
            try:
                with open(file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Ошибка при чтении файла: {e}")
                return []
        return []

    @staticmethod
    def python_to_json(obj: List, file = FILE) -> bool:
        try:
            with open(file, 'w', encoding='utf-8') as file:
                json.dump(obj, file, ensure_ascii=False, indent=4)  # Убедитесь, что данные записываются в читаемом формате
            return True
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")
            return False        

class ItemAlreadyExistsError(Exception): pass

class ItemNotFoundError(Exception): pass

class Collection(list):
    def first(self):
        return self[0]
        
    def last(self):
        return self[-1]

      
class BaseModel:
    data_base = DataBaseManager.json_to_python()

    @classmethod
    def change_database(cls, data_base: List) -> None:
        cls.data_base = data_base

    def __post_init__(self):
        self.id = str(uuid.uuid4()) 
        for field in fields(self):
            name = field.name
            value = getattr(self, name)
            if not isinstance(value, field.type):
                raise TypeError(f'Ожидалось {field.type.__name__} для {name}, получили {type(value).__name__}')
    
    @classmethod
    def create_instance(cls, **kwargs) -> 'BaseModel':
        """Создает экземпляр класса из именованных аргументов с правильными типами."""
        converted_data = {}
        for field in fields(cls):
            name = field.name
            value = kwargs.get(name)

            if value is not None:
                try:
                    converted_data[name] = field.type(value)  # Пробуем преобразовать значение к ожидаемому типу
                except (ValueError, TypeError):
                    raise TypeError(f'Ожидалось {field.type.__name__} для {name}, получили {type(value).__name__}')

        return cls(**converted_data)
    
    def __str__(self) -> str: 
        res = self.__dict__
        res['id'] = self.id
        return str(res)

    def create(self) -> None:
        atributes_without_id = self.__dict__.copy()
        del atributes_without_id['id']
        if self.read(**atributes_without_id):
            raise ItemAlreadyExistsError(f'Элемент уже существует')
        
        self.data_base.append(self.__dict__)

    @classmethod
    def read(cls, **kwargs) -> Collection:
        result_list = Collection()
        for database_element in cls.data_base:
            if all(database_element.get(key) == value for key, value in kwargs.items()): 
                instance = cls.create_instance(**database_element)
                instance.id = database_element.get('id')
                result_list.append(instance)
        return result_list

    def update(self, **kwargs) -> None:
        try:
            element_to_change = self.read(id = self.id).first()
        except IndexError:
            raise ValueError('Элемент с таким id не найден')
        for field, new_value in kwargs.items():
            setattr(element_to_change, field, new_value)
        self.delete(id = self.id)
        element_to_change.create()

    @classmethod
    def delete(cls, id: str) -> dict:
        try:
            element_to_delete = cls.read(id = id).first()
        except IndexError:
            raise ValueError('Элемент с таким id не найден')
        cls.data_base.remove(element_to_delete.__dict__)
        return element_to_delete.__dict__

    @classmethod
    def read_all(cls) -> dict:
        return cls.data_base

    @classmethod
    def save_changes_to_file(cls) -> None:
        DataBaseManager.python_to_json(cls.data_base)
