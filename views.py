from models import Book
from src.tools import type_converter, delete_empty_args

SECCESS = 'Команда успешно выполнена'

@type_converter
def add_book(title:str, author: str, year: int) -> str:
    book = Book.read(title=title,author=author,year=year)
    if book:
        return 'Книга уже существует'
    
    book = Book(title=title,author=author,year=year)
    book.create()

    return SECCESS
    
def delete_book(id: str) -> str:
    book = Book.read(id=id)
    try:
        book = book.first()
        book.delete(id=id)
    except IndexError:
        return 'Книга с таким айди не существует'
    
    return SECCESS
    
@type_converter
def search_book(title: str, author: str, year: int) -> str:
    arguments = delete_empty_args(title=title, author=author,year=year)
    try:
        book = Book.read(**arguments).first()
    except IndexError:
        return 'Такой книги не существует'
    
    return book

def view_all_books() -> str:
    books = Book.read_all()

    return books

def change_book_status(id: str, new_status: str) -> str:
    books = Book.read(id=id)
    try:
        book = books.first()
    except IndexError:
        return 'Книга с таким айди не существует'
    
    if new_status.lower() in ['в наличии', 'вналичии']:
        book.update(id=id, status=True)
    elif new_status.lower() == 'отсутствует':
        book.update(id=id, status=False)
    else:
        return 'Неверный формат команды (Напишите в наличии или отсутствует)'
    
    return SECCESS
