import inspect
from typing import List, Callable

def path(func: Callable, arg_names : List = None, info: str = 'Тут все просто') -> dict:
    """Создает словарь с информацией о функции."""
    res = {
        'func': func,
        'info': info,
    }

    if arg_names:
        res['arg_names'] = arg_names

    return res

def type_converter(func: Callable) -> Callable:
    """Декоратор, который преобразует типы аргументов функции согласно аннотациям типов."""
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)

        converted_args = []
        for param_name, param_value in bound_args.arguments.items():
            param_annotation = sig.parameters[param_name].annotation
            
            if param_annotation is not inspect.Parameter.empty:
                try:
                    converted_args.append(param_annotation(param_value))
                except Exception as e:
                    raise ValueError(f"Ошибка преобразования типов параметра `{param_name}`: {e}")
            else:
                converted_args.append(param_value)

        return func(*converted_args, **{k: v for k, v in kwargs.items() if k not in bound_args.arguments})
    return wrapper

def delete_empty_args(**kwargs):
    """Удаляет аргументы с пустыми значениями из словаря."""
    return {key: value for key, value in kwargs.items() if value}
