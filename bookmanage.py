library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    library.append({'title': title, 'author': author})
    print(f"Book '{title}' added!")

def view_books():
    if not library:
        print("No books in the library.")
    else:
        for idx, book in enumerate(library, start=1):
            print(f"{idx}. {book['title']} by {book['author']}")

def delete_book():
    title = input("Enter the title of the book to delete: ")
    for book in library:
        if book['title'] == title:
            library.remove(book)
            print(f"Book '{title}' deleted!")
            return
    print("Book not found.")

while True:
    print("\nLibrary Menu:")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
        
    