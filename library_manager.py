import json
from datetime import datetime
from collections import Counter
from tabulate import tabulate

# -----------------------------
# Data Persistence
# -----------------------------
books = []

def load_books(filename="books.json"):
    global books
    try:
        with open(filename, "r") as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []
        save_books(filename)

def save_books(filename="books.json"):
    with open(filename, "w") as f:
        json.dump(books, f, indent=4)

# -----------------------------
# Display Helpers (Tabulate)
# -----------------------------
def display_book(book):
    if not book:
        print("Book not found.")
        return
    headers = ["BookID", "Title", "Author", "IsAvailable", "DueDate"]
    rows = [[book["BookID"], book["Title"], book["Author"], book["IsAvailable"], book["DueDate"]]]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def display_books(book_list):
    if not book_list:
        print("No books found.")
        return
    headers = ["BookID", "Title", "Author", "IsAvailable", "DueDate"]
    rows = [[b["BookID"], b["Title"], b["Author"], b["IsAvailable"], b["DueDate"]] for b in book_list]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def display_authors(author_list):
    if not author_list:
        print("No data yet.")
        return
    headers = ["Author", "Checkout Count"]
    print(tabulate(author_list, headers=headers, tablefmt="grid"))

def display_stats(percentage):
    headers = ["Checked Out %"]
    print(tabulate([[f"{percentage:.2f}%"]], headers=headers, tablefmt="grid"))

# -----------------------------
# Core Functions
# -----------------------------
def find_book_by_title(title, books):
    for book in books:
        if book["Title"].lower() == title.lower():
            return book
    return None

def get_overdue_books(books):
    today = datetime.today().date()
    overdue = [
        book for book in books
        if book["DueDate"] and datetime.strptime(book["DueDate"], "%Y-%m-%d").date() < today
    ]
    return sorted(overdue, key=lambda x: x["DueDate"])

def percentage_checked_out(books):
    total = len(books)
    checked_out = sum(1 for book in books if not book["IsAvailable"])
    return (checked_out / total) * 100 if total > 0 else 0

def most_popular_authors(books):
    authors = [book["Author"] for book in books if not book["IsAvailable"]]
    return Counter(authors).most_common()

# -----------------------------
# Book Management
# -----------------------------
def add_book(book_id, title, author):
    books.append({
        "BookID": book_id,
        "Title": title,
        "Author": author,
        "IsAvailable": True,
        "DueDate": None
    })
    print(f"Book '{title}' added successfully.")

def checkout_book(book_id, due_date):
    for book in books:
        if book["BookID"] == book_id and book["IsAvailable"]:
            book["IsAvailable"] = False
            book["DueDate"] = due_date
            print(f"Book '{book['Title']}' checked out until {due_date}.")
            return
    print("Book not available or already checked out.")

def return_book(book_id):
    for book in books:
        if book["BookID"] == book_id and not book["IsAvailable"]:
            book["IsAvailable"] = True
            book["DueDate"] = None
            print(f"Book '{book['Title']}' returned successfully.")
            return
    print("Book not found or already available.")

def delete_book(book_id):
    global books
    for book in books:
        if book["BookID"] == book_id:
            books.remove(book)
            print(f"Book '{book['Title']}' deleted successfully.")
            return
    print("Book not found.")

# -----------------------------
# Menu System
# -----------------------------
def menu():
    load_books()
    while True:
        print("\n--- Library Manager ---")
        print("1. Search book by title")
        print("2. View overdue books")
        print("3. Checkout statistics")
        print("4. Popular authors")
        print("5. Add new book")
        print("6. Checkout book")
        print("7. Return book")
        print("8. Save & Exit")
        print("9. Delete book")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            book = find_book_by_title(title, books)
            display_book(book)
        elif choice == "2":
            overdue = get_overdue_books(books)
            display_books(overdue)
        elif choice == "3":
            display_stats(percentage_checked_out(books))
        elif choice == "4":
            popular = most_popular_authors(books)
            display_authors(popular)
        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            add_book(book_id, title, author)
        elif choice == "6":
            book_id = int(input("Enter Book ID to checkout: "))
            due_date = input("Enter due date (YYYY-MM-DD): ")
            checkout_book(book_id, due_date)
        elif choice == "7":
            book_id = int(input("Enter Book ID to return: "))
            return_book(book_id)
        elif choice == "8":
            save_books()
            print("Library data saved. Goodbye!")
            break
        elif choice == "9":
            book_id = int(input("Enter Book ID to delete: "))
            delete_book(book_id)
        else:
            print("Invalid choice. Try again.")

# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    menu()