import sqlite3
import datetime
import os
from langdetect import detect
conn = sqlite3.connect('flameLibrary.db')


print("welcome to the Library Management System! \n")
today = datetime.datetime.now()
today = today.strftime("%Y-%m-%d")
print(today)

print("Borrowers Late on Return: ")
output = conn.execute("SELECT * FROM borrowers WHERE toReturn_date < ? AND Return_date is NULL",(today,))
row = output.fetchone()
while row is not None:
    print(str(row) + "\n")
    row = output.fetchone()


while True:
    print("select command: ")
    command = input("Search (s) --- Borrow a book (b) --- add a book (a) --- remove a book (r) --- return book (rb) \n $")

    
    if command == "s":       
        choice = input("search for author (a) / book (b) ? ")
        if choice == "a":
            spec = input("Search query: ")
            output = conn.execute("SELECT * FROM books WHERE author LIKE '%{0}%'".format(spec))
            rows = output.fetchall()

            for row in rows:
                row_str = ' '.join(str(item) for item in row)
                if detect(row_str) == 'ar':
                    reversed_row = tuple(str(item)[::-1] for item in row)  # Reverse each item in the row
                    print(str(reversed_row) + "\n")
                    #prints arabic text properly
                else:
                    print(str(row) + "\n")
            




            
        elif choice == "b":
            spec = input("Search query: ")
            output = conn.execute("SELECT * FROM books WHERE bookname LIKE '%{0}%'".format(spec))
            
            rows = output.fetchall()
            for row in rows:
                row_str = ' '.join(str(item) for item in row)
                if detect(row_str) == 'ar':
                    reversed_row = tuple(str(item)[::-1] for item in row)  # Reverse each item in the row
                    print(str(reversed_row) + "\n")
                    #prints arabic text properly
                else:
                    print(str(row) + "\n")



    if command == "b":
        bookid = input("Book id to borrow / or enter 'lb' to view current borrowers: ")
        if bookid == "lb":
            output = conn.execute("SELECT * FROM borrowers WHERE Return_date is NULL")
            row = output.fetchone()
            while row is not None:
                print(str(row) + "\n")
                row = output.fetchone()
            
                
                    

        
        else:
            output = conn.execute("SELECT availability FROM books WHERE book_id=?", (bookid,))       
            isAvailable = output.fetchone()
            if isAvailable is not None:
                isAvailable = isAvailable[0] 
                print(isAvailable)

            if isAvailable == 1:
                print("Book is available \n")

                nameBorrower = input("enter borrower name: ")
                phonenumber = input("enter phone number: ")

                today = datetime.datetime.now()
                borrowed_date = today.strftime("%Y %m %d")

                toReturn_date = input("enter return date YYYY-MM-DD: ")
                output = conn.execute("SELECT bookname FROM books WHERE book_id=?", (bookid,))
                bookname = output.fetchone()[0]
                conn.execute("INSERT INTO borrowers (borrower_name, borrower_phonenumber, book_id, bookname, borrowed_date, toReturn_date) VALUES (?, ?, ?, ?, ?, ?)", (nameBorrower, phonenumber, bookid, bookname, borrowed_date, toReturn_date))
                conn.execute("UPDATE books SET availability = '0' WHERE book_id = ?;", (bookid,))
                conn.commit()
        


            elif isAvailable == 0:
                print("Book is currently unavailable \n")
            else:
                print("Book id not found in the database")


    elif command == "a":
        bname = input("enter book name: ")
        author = input("enter author name: ")
        genre = input("enter genre: ")
        location = input("enter location: ")
        conn.execute("INSERT INTO books(bookname, author, genre, Location) VALUES (?,?,?,?)",(bname, author, genre, location))
        conn.commit()
        print("shit added")
    

    elif command == "r":
        bookid = input("enter book id to remove:")
        conn.execute("DELETE FROM books WHERE book_id= ?", (bookid,))
        conn.commit()
        print("Book deleted successfully")
        
    elif command == "rb":
        bookid = input("enter book id to return: ")
        output = conn.execute("SELECT availability FROM books WHERE book_id=?", (bookid,))       
        isAvailable = output.fetchone()
        if isAvailable is not None:
            isAvailable = isAvailable[0] 
            print(isAvailable)
        
        if isAvailable == 1:
            print("book already returned")
        elif isAvailable == 0:
            confirmation = input("are you sure you want to return this book? (y/n) ")
            if confirmation == 'y':
                conn.execute("UPDATE books SET availability = '1' WHERE book_id = ?;", (bookid,))

                today = datetime.datetime.now()
                returndate = today.strftime("%Y %m %d")
    
                conn.execute("UPDATE borrowers SET return_date = ? WHERE book_id = ?;", (returndate, bookid,))
                conn.commit()
                print("book returned")
        else:
            print("book id not found")

    if command == "clear":
        os.system('cls')



