import pandas as pd
import sqlite3

# change the name to your excel file 
books = pd.read_excel(  
    'sampleData.xlsx', 
    sheet_name='data (9)',
    header=0)



conn = sqlite3.connect('flameLibrary.db')
        
for index, row in books.iterrows():
    print(row)
    conn.execute('INSERT INTO books (bookname, author, genre, Location, availability) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], row[4]))

conn.commit()
conn.close()  

