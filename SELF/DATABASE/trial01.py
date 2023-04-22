import sqlite3

con = sqlite3.connect("tutorial4.db")

cur = con.cursor()

cur.execute("CREATE TABLE movies(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

res = cur.execute("SELECT name FROM sqlite_master WHERE name = 'spam'")
res.fetchone()is None

cur.execute("""
    INSERT INTO movies VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit()

res = cur.execute("SELECT score FROM movies")
res.fetchall()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brain", 1979, 8.0),
]

cur.executemany("INSERT INTO movies VALUES(?, ?, ?)", data)
con.commit() # Remember to commit the transaction after executing INSERT

for row in cur.execute("SELECT year, title FROM movies ORDER BY year"):
    print(row)

con.close()
new_con = sqlite3.connect("tutorial2.db")
new_cur = new_con.cursor()
new_cur.execute("SELECT title, year FROM movies ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movies is {title!r}, released in {year}')

