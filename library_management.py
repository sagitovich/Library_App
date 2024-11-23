import os
import json
from datetime import datetime

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self) -> list:
        """Загрузка данных из JSON-файла."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_books(self):
        """Сохранение данных в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

    def add_book(self):
        """Добавление новой книги"""
        title = input("Название книги: ").strip()
        author = input("Автор книги: ").strip()
        year = input("Год издания: ").strip()

        if not year.isdigit():
            print("Год должен быть числом!")
            return
        
        if int(year) > datetime.now().year:
            print("Книга не может быть из будущего :)")

        book_id = len(self.books) + 1
        self.books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "year": int(year),
            "status": "в наличии"
        })
        self.save_books()
        print(f"Книга добавлена")

    def delete_book(self):
        """Удаление книги по ID"""
        try:
            book_id = int(input("Введите ID книги для удаления: "))
            book = next((i for i in self.books if i["id"] == book_id), None)

            if book:
                self.books.remove(book)
                self.save_books()
                print(f"Книга удалена")
            else:
                print("Книга с таким ID не найдена.")
        except ValueError:
            print("ID должен быть числом!")

    def search_book(self):
        """Поиск книги по заголовку, автору или году"""
        query = input("Введите название, автора или год написания книги: ").strip()
        results = [
            i for i in self.books
            if query.lower() in str(i["title"]).lower()
            or query.lower() in str(i["author"]).lower()
            or query == str(i["year"])
        ]

        if results:
            print("Результаты поиска:")
            for book in results:
                self.print_book(book)
        else:
            print("Книг по данному запросу не найдено.")

    def show_all_books(self):
        """Отображение всех книг"""
        if not self.books:
            print("Не найдено ни одной книги.")
        else:
            print("Список всех книг:")
            for book in self.books:
                self.print_book(book)

    def update_status(self):
        """Обновление статуса книги"""
        try:
            book_id = int(input("Введите ID книги для изменения статуса: "))
            book = next((i for i in self.books if i["id"] == book_id), None)

            if book:
                if book["status"] == "в наличии":
                    book["status"] = "выдана"
                else:
                    book["status"] = "в наличии"
                self.save_books()
                print(f"Статус книги обновлен!")
            else:
                print("Книга с таким ID не найдена.")
        except ValueError:
            print("ID должен быть числом!")

    @staticmethod
    def print_book(book):
        """Вывод информации о книге"""
        print(f"ID: {book['id']} | {book['title']} | {book['author']} | {book['year']} | {book['status']}")


def show_menu():
    print("""
Возможные действия:
┏ 1. Добавить книгу
┣ 2. Удалить книгу
┣ 3. Найти книгу 
┣ 4. Показать все книги 
┣ 5. Обновить статус книги
┗ 6. Выйти из приложения
    """)
