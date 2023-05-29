import sqlite3

# Create a connection to database called "ebookstore"
db = sqlite3.connect('ebookstore.db')

# Create a cursor object
cursor = db.cursor()

# Create the table called "books" if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Title VARCHAR(255),
               Author VARCHAR(255),
               Qty INTEGER
            )''')

# Add data into the "books" table
cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES ('A Tale of Two Cities', 'Charles Dickens', 30)")
cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES ('Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40)")
cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES ('The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25)")
cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES ('The Lord of the Rings', 'J.R.R Tolkien', 37)")
cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES ('Alice in Wonderland', 'Lewis Carroll', 12)")

# Create a function for the menu
# print Welcome message and options
def menu():
    print("Welcome!")
    print("1 ~ Add book")
    print("2 ~ Update book info")
    print("3 ~ Delete book")
    print("4 ~ Search for book")
    print("5 ~ Exit")
    # prompt user input choice
    choice = input("Enter your choice: ")
    # return the choice
    return choice

# Create a function to add a book
def add_book():
    # prompt user enter book info
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    # execute the sql insert statement for new user input
    cursor.execute("INSERT INTO books (Title, Author, Qty) VALUES (?, ?, ?)", (title, author, qty))
    # commit the change
    db.commit()
    # print completed message
    print("Completed!")

# Create a function to update a book
def update_book():
    # prompt user enter ID of book to be update
    book_id = int(input("Enter book ID: "))
    # prompt user enter updated book info
    title = input("Enter updated book title: ")
    author = input("Enter updated book author: ")
    qty = int(input("Enter updated book quantity: "))
    # execute the sql update statement for the new user input
    cursor.execute("UPDATE books SET Title=?, Author=?, Qty=? WHERE id=?", (title, author, qty, book_id))
    # commit the changes
    db.commit()
    # print completed message
    print("Completed!")

# Create a function to delete a book
def delete_book():
    # prompt user enter ID of book to be deleted
    book_id = int(input("Enter book ID: "))
    # execute the sql delete statement for user input for the book
    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
    # commit changes
    db.commit()
    # print deleted message
    print("Deleted!")

# Create a function to search for a book
def search_books():
    # prompt user input a keyword that is in the book info
    keyword = input("Enter search keyword: ")
    # execute the sql select statement for user input book search
    cursor.execute("SELECT * FROM books WHERE Title LIKE ? OR Author LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
    # fetch all the rows with the user input info
    rows = cursor.fetchall()
    # if there is no rows print "books not found"
    if len(rows) == 0:
        print("Books not found.")
    # else iterate over rows and print each one
    else:
        for row in rows:
            print(row)

# Create a while loop for the Menu
# call the functions for the if and elif statements
while True:
    choice = menu()
    if choice == '5':
        break
    elif choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_books()
    else:
        # print error message
        print("Invalid option! Please try again.")

