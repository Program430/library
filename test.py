import unittest
from views import add_book, delete_book, search_book, view_all_books, change_book_status 
from models import Book

class TestLibraryViews(unittest.TestCase):
    def setUp(self):
        self.test_data_base = [{
            "title": "название",
            "author": "автор",
            "year": 2000,
            "status": True,
            "id": "cb51ffb5-ecd6-4a91-bdcc-36f79237beb1"
        }]
        Book.change_database(self.test_data_base)

    def test_add_book_success(self):
        title = "Test Book"
        author = "Test Author"
        year = 2020

        result = add_book(title, author, year)

        self.assertEqual(result, 'Команда успешно выполнена')
        self.assertEqual(len(Book.data_base), 2) 

    def test_add_duplicate_book(self):
        title = "название"  
        author = "автор"    
        year = 2000        

        result = add_book(title, author, year)

        self.assertEqual(result, 'Книга уже существует')  
        self.assertEqual(len(Book.data_base), 1)  

    def test_delete_book_success(self):
        book_id = "cb51ffb5-ecd6-4a91-bdcc-36f79237beb1"

        result = delete_book(book_id)

        self.assertEqual(result, 'Команда успешно выполнена')
        self.assertEqual(len(Book.data_base), 0)  

    def test_delete_nonexistent_book(self):
        result = delete_book("nonexistent-id")

        self.assertEqual(result, 'Книга с таким айди не существует')
        self.assertEqual(len(Book.data_base), 1)  

    def test_search_book_success(self):
        title = "название"
        
        author = "автор"
        year = 2000

        result = search_book(title=title, author=author, year=year)

        self.assertIsInstance(result, Book) 
        self.assertEqual(result.title, title)  

    def test_search_nonexistent_book(self):
        result = search_book(title="nonexistent", author="nonexistent", year=2023)

        self.assertEqual(result, 'Такой книги не существует')

    def test_view_all_books(self):
        result = view_all_books()

        self.assertIsInstance(result, list)  
        self.assertEqual(len(result), 1)  
        
    def test_change_book_status_success(self):
        book_id = "cb51ffb5-ecd6-4a91-bdcc-36f79237beb1"

        result = change_book_status(book_id, "отсутствует")

        self.assertEqual(result, 'Команда успешно выполнена')
        self.assertFalse(Book.data_base[0]["status"])

    def test_change_book_status_nonexistent(self):
        result = change_book_status("nonexistent-id", "в наличии")

        self.assertEqual(result, 'Книга с таким айди не существует')

    def test_change_book_status_invalid_input(self):
        book_id = "cb51ffb5-ecd6-4a91-bdcc-36f79237beb1"

        result = change_book_status(book_id, "invalid status")

        self.assertEqual(result, 'Неверный формат команды (Напишите в наличии или отсутствует)')


if __name__ == '__main__':
    unittest.main()

