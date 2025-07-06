class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} [ISBN: {self.isbn}, Copies: {self.copies}]"


class Library:
    def __init__(self):
        self.books = {}  # ISBN -> Book

    def add_book(self, title, author, isbn, copies):
        if isbn in self.books:
            self.books[isbn].copies += copies
        else:
            self.books[isbn] = Book(title, author, isbn, copies)
        print(f"\n Book '{title}' added successfully.")

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"\n Book with ISBN {isbn} removed.")
        else:
            print("\n Book not found.")

    def search_book(self, keyword):
        found = False
        print("\n🔍 Search Results:")
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(f" - {book}")
                found = True
        if not found:
            print("No matching books found.")

    def issue_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            if book.copies > 0:
                book.copies -= 1
                print(f"\n Book '{book.title}' issued successfully.")
            else:
                print("\n❌ No copies available.")
        else:
            print("\n❌ Book not found.")

    def return_book(self, isbn):
        if isbn in self.books:
            self.books[isbn].copies += 1
            print(f"\n Book '{self.books[isbn].title}' returned successfully.")
        else:
            print("\n❌ Book not found in library.")

    def list_books(self):
        if not self.books:
            print("\n No books in the library.")
            return
        print("\n📚 All Books:")
        for book in self.books.values():
            print(f" - {book}")



def main():
    lib = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. List All Books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            copies = int(input("Number of copies: "))
            lib.add_book(title, author, isbn, copies)

        elif choice == "2":
            isbn = input("Enter ISBN to remove: ")
            lib.remove_book(isbn)

        elif choice == "3":
            keyword = input("Enter title or author to search: ")
            lib.search_book(keyword)

        elif choice == "4":
            isbn = input("Enter ISBN to issue: ")
            lib.issue_book(isbn)

        elif choice == "5":
            isbn = input("Enter ISBN to return: ")
            lib.return_book(isbn)

        elif choice == "6":
            lib.list_books()

        elif choice == "0":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
