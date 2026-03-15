import json
import sys
import os
from datetime import datetime, timedelta

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from library_manager import LibraryManager


def test_add_book(tmp_path):
    test_file = tmp_path / "books.json"
    manager = LibraryManager(str(test_file))

    manager.add_book("1984", "George Orwell", 1949)

    with open(test_file, "r") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["title"] == "1984"
    assert data[0]["author"] == "George Orwell"
    assert data[0]["year"] == 1949


def test_search_books(tmp_path):
    test_file = tmp_path / "books.json"
    manager = LibraryManager(str(test_file))

    manager.add_book("Dune", "Frank Herbert", 1965)
    manager.add_book("Foundation", "Isaac Asimov", 1951)

    results = manager.search_books("Dune")

    assert len(results) == 1
    assert results[0]["author"] == "Frank Herbert"


def test_checkout_and_return(tmp_path):
    test_file = tmp_path / "books.json"
    manager = LibraryManager(str(test_file))

    manager.add_book("The Hobbit", "J.R.R. Tolkien", 1937)
    manager.checkout_book("The Hobbit")
    assert manager.books[0]["status"] == "borrowed"

    manager.return_book("The Hobbit")
    assert manager.books[0]["status"] == "available"


def test_delete_book(tmp_path):
    test_file = tmp_path / "books.json"
    manager = LibraryManager(str(test_file))

    manager.add_book("Brave New World", "Aldous Huxley", 1932)
    manager.delete_book("Brave New World")

    assert len(manager.books) == 0


def test_overdue_books(tmp_path):
    test_file = tmp_path / "books.json"
    manager = LibraryManager(str(test_file))

    # Add a book and set it overdue
    manager.add_book("Catch-22", "Joseph Heller", 1961)
    manager.books[0]["status"] = "borrowed"
    manager.books[0]["due_date"] = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    manager.save_books()

    overdue = manager.get_overdue_books()
    assert len(overdue) == 1
    assert overdue[0]["title"] == "Catch-22"