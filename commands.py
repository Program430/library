from views import add_book, delete_book, search_book, view_all_books, change_book_status
from src.tools import path

commands = {
    'add': path(add_book, arg_names = ['Название','Автор','Год'], info = 'Команда для добавления книги.'),
    'delete': path(delete_book, arg_names = ['id'], info = 'Команда для удаления книги.'),
    'search': path(search_book, arg_names = ['Название(Необязательный)','Автор(Необязательный)','Год(Необязательный)'], info = 'Команда для поиска книги. Ненужный параметр пропустите.'),
    'view': path(view_all_books, info = 'Команда для просмотра всех книг.'),
    'change': path(change_book_status, arg_names = ['id', 'Статус'], info = 'Команда для изменения книги.'),
}

