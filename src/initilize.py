from commands import commands
from src.database import BaseModel

class Initialazer:
    def __init__(self) -> None:
        self.commands = commands
        # Можно добавить еще специфических команд
        self.commands.update(self._file_save_command())
        self.commands.update(self._helper_command())

    def _file_save_command(self) -> dict:
        return {'fsave':{
            'func': BaseModel.save_changes_to_file,
            'info': 'Необходима для сохранения данных в файл.'
        }}
    
    def _helper_command(self) -> dict:
        help_info = 'Список команд:\n'
        for command_name, command_dict in self.commands.items():
            help_info += f'{command_name} {command_dict['info']}\n'

        return {'help':{
            'func': lambda : help_info,
            'info': 'Необходима для получения информации о командах.'
        }}

