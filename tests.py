import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_name_more_40_symb_did_not_add(self):
        collector = BooksCollector()
        collector.add_new_book('В названии этой книги названии 44 символа!!')
        result=collector.get_books_genre()
        assert len(result)==0

    @pytest.mark.parametrize('book_name', ['Книга без жанра','Ужасная книга стоматологов', 'Космический Джем'])
    def test_add_new_book_without_genre_added(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        result=collector.get_books_genre()
        expected={book_name:''}
        assert result==expected

    def test_book_without_genre_not_added_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')
        result=collector.get_books_for_children()
        assert len(result)==0

    def test_add_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.set_book_genre('Ужасная книга стоматологов', 'Ужасы')
        collector.set_book_genre('Космический Джем', 'Фантастика')
        result=collector.get_books_genre()
        expected={'Ужасная книга стоматологов':'Ужасы', 'Космический Джем':'Фантастика'}
        assert result==expected

    def test_fears_not_added_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.set_book_genre('Ужасная книга стоматологов', 'Ужасы')
        collector.set_book_genre('Космический Джем', 'Фантастика')
        result=collector.get_books_for_children()
        expected=['Космический Джем']
        assert result==expected

    def test_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.add_book_in_favorites('Космический Джем')
        collector.add_book_in_favorites('Ужасная книга стоматологов')
        result=collector.get_list_of_favorites_books()
        assert len(result)==2

    def test_unknown_book_not_added_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.add_book_in_favorites('Космический Джем')
        collector.add_book_in_favorites('Неопознанная книга')
        result=collector.get_list_of_favorites_books()
        expected=['Космический Джем']
        assert result==expected

    def test_delete_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.add_book_in_favorites('Космический Джем')
        collector.add_book_in_favorites('Ужасная книга стоматологов')
        collector.delete_book_from_favorites('Космический Джем')
        result=collector.get_list_of_favorites_books()
        assert len(result)==1

    def test_delete_unknown_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.add_book_in_favorites('Космический Джем')
        collector.add_book_in_favorites('Ужасная книга стоматологов')
        collector.delete_book_from_favorites('Неопознанная книга')
        result=collector.get_list_of_favorites_books()
        assert len(result)==2

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.set_book_genre('Ужасная книга стоматологов', 'Ужасы')
        collector.set_book_genre('Космический Джем', 'Фантастика')
        result=collector.get_books_with_specific_genre('Ужасы')
        expected=['Ужасная книга стоматологов']
        assert result==expected

    def test_unknown_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Ужасная книга стоматологов')
        collector.add_new_book('Космический Джем')
        collector.set_book_genre('Ужасная книга стоматологов', 'Чудеса')
        collector.set_book_genre('Космический Джем', 'Фантастика')
        result=collector.get_books_genre()
        expected={'Ужасная книга стоматологов':'', 'Космический Джем':'Фантастика'}
        assert result==expected