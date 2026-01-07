

library = []
students = []


def users_login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "admin@98":

        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials.\n")
        return False



def register_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")

    student = {
        "id": student_id,
        "name": name,
        "dept": dept
    }

    students.append(student)
    print("Student registered successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students registered.\n")
        return

    print("\nRegistered Students:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Department: {s['dept']}")
    print()


# -------- Book Module --------
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "issued": False,
        "issued_to": None
    }

    library.append(book)
    print("Book added successfully!\n")


def view_books():
    if len(library) == 0:
        print("No books available in the library.\n")
        return

    print("\nLibrary Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        issued_to = book["issued_to"] if book["issued_to"] else "None"
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, "
              f"Status: {status}, Issued To: {issued_to}")
    print()


def issue_book():
    book_id = input("Enter Book ID: ")
    student_id = input("Enter Student ID: ")

    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                print("Book already issued.\n")
                return

            for s in students:
                if s["id"] == student_id:
                    book["issued"] = True
                    book["issued_to"] = student_id
                    print("Book issued successfully!\n")
                    return

            print("Student not found.\n")
            return

    print("Book not found.\n")


def return_book():
    book_id = input("Enter Book ID: ")

    for book in library:
        if book["id"] == book_id:
            if book["issued"]:
                book["issued"] = False
                book["issued_to"] = None
                print("Book returned successfully!\n")
            else:
                print("Book was not issued.\n")
            return

    print("Book not found.\n")


# -------- Main Menu --------
def menu():
    while True:
        print("Library Management System")
        print("1. Register Student")
        print("2. View Students")
        print("3. Add Book")
        print("4. View Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            add_book()
        elif choice == "4":
            view_books()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            return_book()
        elif choice == "7":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.\n")



if users_login():


    menu()




else:
    print("Access denied.")
