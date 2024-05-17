import sqlite3
conn = sqlite3.connect('flameLibrary.db')
        
conn.execute("""
    CREATE TABLE books(
        book_id INTEGER PRIMARY KEY,     
        bookname TEXT,
        author TEXT,
        genre TEXT,
        location TEXT,
        availability INTEGER DEFAULT '1',
        UNIQUE(bookname) ON CONFLICT IGNORE
        )   

# location is meant to be a 2 character id to identify the location of the book: "A1". the letter specifying which bookshelf is it in
# and the number specifiying in which shelf is the book in.
    """)
conn.execute("""
    CREATE TABLE borrowers(  
        borrower_name TEXT,
        borrower_phonenumber TEXT,
        book_id INTEGER,
        bookname TEXT,
        borrowed_date TEXT,
        toReturn_date TEXT,
        Return_date TEXT)   


    """)

#conn.execute('CREATE TABLE books (bookname TEXT, author TEXT, genre TEXT)')    
conn.commit()
conn.close()  

