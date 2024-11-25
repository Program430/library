from src.initilize import Initialazer
from typing import Tuple

class Manager:
    initialazer = Initialazer()

    @classmethod
    def find_command(cls, command: str) -> tuple:
        if command in cls.initialazer.commands:
            about_command = cls.initialazer.commands[command]
            command_args = about_command['arg_names'] if 'arg_names' in about_command else []
            return (about_command['func'], command_args)
        else:
            return ()

    @classmethod
    def start(cls) -> None:
        print("\nДобро пожаловать в книжный менеджер!\nДля просмотра всех команд используйте \'help\'")

        while True:
            user_input = input('Type command:')

            command_typle= cls.find_command(user_input)

            if command_typle:
                view_function, argument_names = command_typle
            else:
                print('Команда не найдена!')
                continue
            
            argument_buffer = []
            for i in argument_names:
                user_args_input = input(i + ' ')
                argument_buffer.append(user_args_input)

            try:
                view_function_result = view_function(*argument_buffer)
            except ValueError as e:
                print(e.value)
                continue

            print(view_function_result)