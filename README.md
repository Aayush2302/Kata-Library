# Library Management System

## Overview
This Library Management System is a Python-based project designed to handle book and user management for a library. The system enforces role-based access control, allowing Admins, Librarians, and Members to perform different actions based on their roles. It includes functionality for adding, removing, borrowing, and returning books, as well as managing user accounts.

## Features
- **Role-based Access Control**:
  - **Admin**: Can add and remove users, as well as add and remove books.
  - **Librarian**: Can add and remove books.
  - **Member**: Can borrow and return books.

- **Book Management**:
  - Add and remove books from the catalog.
  - Borrow and return books, with stock tracking.
  - View available books in the catalog.

- **User Management**:
  - Add and remove users.
  - View a list of all registered users.



  ```bash
  PROJECT STRUCTURE
  Library/
  ├── main/
  │   ├── Book.py
  │   ├── User.py
  │   ├── Library.py
  ├── test/
  │   ├── test_book.py
  │   ├── test_library.py
  ├── test_reports/
  │   ├── test_library_reports.xml
  │   ├── test_book_reports.xml
  └── README.md

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Aayush2302/Kata-Library

2. Running the Application
   ```bash
   python main/Library.py


