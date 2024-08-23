import json

def get_books_by_genre(genre):
    # Read the list of books from the file
    with open('books.json', 'r') as file:
        books = json.load(file)
    
    # Filter books by the given genre
    filtered_books = [book for book in books if book["genre"].lower() == genre.lower()]
    
    print(filtered_books)