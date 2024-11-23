from library_management import show_menu, Library


def main():
    manager = Library()

    while True:
        show_menu()
        action = int(input("Выберете нужное: "))

        if action == 1:
            manager.add_book()
        elif action == 2:
            manager.delete_book()
        elif action == 3:
            manager.search_book()
        elif action == 4:
            manager.show_all_books()
        elif action == 5:
            manager.update_status()
        else:
            exit()


if __name__ == "__main__":
    main()
