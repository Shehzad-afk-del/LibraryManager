import json
from datetime import datetime, timedelta
from tabulate import tabulate


class LibraryManager:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    # -------------------------------
    # Persistence
    # -------------------------------
    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []
            self.save_books()

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump(self.books, f, indent=4)

    # -------------------------------
    # Core Operations
    # -------------------------------
    def add_book(self, title, author, year):
        book = {
            "title": title,
            "author": author,
            "year": year,
            "status": "available",
            "due_date": None
        }
        self.books.append(book)
        self.save_books()

    def search_books(self, query):
        return [b for b in self.books if query.lower() in b["title"].lower()]

    def delete_book(self, title):
        self.books = [b for b in self.books if b["title"] != title]
        self.save_books()

    def checkout_book(self, title, days=14):
        for b in self.books:
            if b["title"] == title and b["status"] == "available":
                b["status"] = "borrowed"
                b["due_date"] = (datetime.today() + timedelta(days=days)).strftime("%Y-%m-%d")
                self.save_books()
                return True
        return False

    def return_book(self, title):
        for b in self.books:
            if b["title"] == title and b["status"] == "borrowed":
                b["status"] = "available"
                b["due_date"] = None
                self.save_books()
                return True
        return False

    def get_overdue_books(self):
        overdue = []
        today = datetime.today().date()
        for b in self.books:
            if b["status"] == "borrowed" and b["due_date"]:
                due_date = datetime.strptime(b["due_date"], "%Y-%m-%d").date()
                if due_date < today:
                    overdue.append(b)
        return overdue

    # -------------------------------
    # Display Helpers
    # -------------------------------
    def display_books(self):
        if not self.books:
            print("No books in library.")
            return
        headers = ["Title", "Author", "Year", "Status", "Due Date"]
        rows = [[b["title"], b["author"], b["year"], b["status"], b["due_date"]] for b in self.books]
        print(tabulate(rows, headers=headers, tablefmt="grid"))