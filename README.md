# 📚 LibraryManager
![Tests](https://github.com/Shehzad-afk-del/LibraryManager/actions/workflows/tests.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub stars](https://img.shields.io/github/stars/Shehzad-afk-del/LibraryManager?style=social)
![GitHub forks](https://img.shields.io/github/forks/Shehzad-afk-del/LibraryManager?style=social)
![Issues](https://img.shields.io/github/issues/Shehzad-afk-del/LibraryManager)

LibraryManager is a lightweight Python CLI tool for managing personal book collections.  
It supports adding, searching, checking out, returning, deleting books, tracking overdue items, and generating statistics.  
Data is stored in JSON with clean tabular output via [tabulate](https://pypi.org/project/tabulate/).

---

## 🚀 Features
- Add new books with details (title, author, year, etc.)
- Search books by title or author
- Checkout and return books
- Delete books from the collection
- Track overdue items
- View statistics (total books, borrowed books, etc.)

---

## 🛠 Installation
Clone the repository:
```bash
git clone https://github.com/Shehzad-afk-del/LibraryManager.git
cd LibraryManager

pip install -r requirements.txt

LibraryManager/
├── books.json            # Data storage
├── library_manager.py    # Main CLI tool
├── requirements.txt      # Dependencies
└── README.md             # Documentation


---

## ✅ Next Step
1. Save this text into your `README.md` file.  
2. Run:
   ```bash
   git add README.md
   git commit -m "Added complete README.md"
   git push
