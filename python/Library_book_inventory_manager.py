import json
import os

# Book Class
class Book:
    def __init__(self, book_id, title, author, issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued = issued

    def to_dict(self):
        return {
            "Book ID": self.book_id,
            "Title": self.title,
            "Author": self.author,
            "Issued": self.issued
        }


# Library Class
class Library:
    FILE_NAME = "library.json"

    def __init__(self):
        self.books = {}
        self.load_books()

    def load_books(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)
                    self.books = data
            except:
                self.books = {}

    def save_books(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = Book(book_id, title, author)

        self.books[book_id] = book.to_dict()
        self.save_books()

        print("Book Added Successfully!")

    def search_book(self):
        keyword = input("Enter Title or Author: ").lower()

        found = False

        print("\nSearch Results")
        print("-" * 60)

        for book in self.books.values():
            if keyword in book["Title"].lower() or keyword in book["Author"].lower():
                status = "Issued" if book["Issued"] else "Available"

                print(f"ID: {book['Book ID']}")
                print(f"Title: {book['Title']}")
                print(f"Author: {book['Author']}")
                print(f"Status: {status}")
                print("-" * 60)

                found = True

        if not found:
            print(" No Matching Books Found!")

    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ")

        if book_id not in self.books:
            print(" Book Not Found!")
            return

        if self.books[book_id]["Issued"]:
            print(" Book Already Issued!")
            return

        self.books[book_id]["Issued"] = True
        self.save_books()

        print(" Book Issued Successfully!")

    def return_book(self):
        book_id = input("Enter Book ID to Return: ")

        if book_id not in self.books:
            print("Book Not Found!")
            return

        if not self.books[book_id]["Issued"]:
            print("Book Was Not Issued!")
            return

        self.books[book_id]["Issued"] = False
        self.save_books()

        print("Book Returned Successfully!")

    def list_books(self):
        if not self.books:
            print("No Books Available!")
            return

        print("\n{:<10} {:<25} {:<20} {:<10}".format(
            "ID", "TITLE", "AUTHOR", "STATUS"))
        print("-" * 70)

        for book in self.books.values():
            status = "Issued" if book["Issued"] else "Available"

            print("{:<10} {:<25} {:<20} {:<10}".format(
                book["Book ID"],
                book["Title"],
                book["Author"],
                status
            ))

    def report(self):
        total_books = len(self.books)

        issued_books = 0

        for book in self.books.values():
            if book["Issued"]:
                issued_books += 1

        available_books = total_books - issued_books

        print("\n===== LIBRARY REPORT =====")
        print(f"Total Books      : {total_books}")
        print(f"Issued Books     : {issued_books}")
        print(f"Available Books  : {available_books}")


# Main Program
def main():
    library = Library()

    while True:
        print("\n===== LIBRARY BOOK INVENTORY MANAGER =====")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. View Report")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.search_book()

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            library.report()

        elif choice == "7":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()