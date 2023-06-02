import csv


def load_books():
    books = []
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'id':
                pass
            else:
                book = {
                    'id': int(row[0]),
                    'title': row[1],
                    'author': row[2],
                    'status': row[3]
                }
                books.append(book)
    return books


def save_books(books):
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'title', 'author', 'status'])
        for book in books:
            writer.writerow([book['id'], book['title'], book['author'], book['status']])


def find_book(books, book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None


def add_book(books, title, author):
    book_id = books[-1]['id'] + 1 if books else 1
    book = {
        'id': book_id,
        'title': title,
        'author': author,
        'status': 'available'
    }
    books.append(book)
    save_books(books)


def remove_book(books, book_id):
    book = find_book(books, book_id)
    if book:
        books.remove(book)
        save_books(books)
        print('Book removed successfully.')
    else:
        print('Book not found.')


def checkout_book(books, book_id):
    book = find_book(books, book_id)
    if book:
        if book['status'] == 'available':
            book['status'] = 'checked out'
            save_books(books)
            print('Book checked out successfully.')
        else:
            print('Book is not available.')
    else:
        print('Book not found.')


def return_book(books, book_id):
    book = find_book(books, book_id)
    if book:
        if book['status'] == 'checked out':
            book['status'] = 'available'
            save_books(books)
            print('Book returned successfully.')
        else:
            print('Book is already available.')
    else:
        print('Book not found.')


def print_books(books):
    if books:
        print('ID\tTitle\t\t\tAuthor\t\t\tStatus')
        print('--\t-----\t\t\t------\t\t\t------')
        for book in books:
            print(f"{book['id']}\t{book['title']}\t\t\t{book['author']}\t\t\t{book['status']}")
    else:
        print('No books found.')


def main():
    books = load_books()
    while True:
        print('\nLibrary Book Management System\n')
        print('1. Add Book')
        print('2. Remove Book')
        print('3. Checkout Book')
        print('4. Return Book')
        print('5. List Books')
        print('6. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            title = input('Enter title: ')
            author = input('Enter author: ')
            add_book(books, title, author)
        elif choice == '2':
            book_id = int(input('Enter book ID: '))
            remove_book(books, book_id)
        elif choice == '3':
            book_id = int(input('Enter book ID: '))
            checkout_book(books, book_id)
        elif choice == '4':
            book_id = int(input('Enter book ID:  '))
            return_book(books, book_id)
        elif choice == '5':
            print_books(books)
        elif choice == '6':
            exit()
        else:
            print('wrong input')


main()
