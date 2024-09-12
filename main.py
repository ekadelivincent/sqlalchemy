import psycopg2

conn = psycopg2.connect(
    dbname="book_manager",
    user="wambua",
    password="wambua",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# cur.execute("SELECT * FROM books;")
# sql ='''INSERT INTO books (id, title, isbn) VALUES(3,'Ego is the enemy',567565);'''
sql = '''INSERT INTO members(id, name, member_id) VALUES (3, 'Cindy Akumu', 103)'''

cur.execute(sql)

conn.commit()
# books = cur.fetchall()

# print(books)

cur.close()
conn.close()