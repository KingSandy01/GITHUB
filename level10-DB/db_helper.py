import sqlite3

db = 'my_todo.db'
table_name = 'tasks'
conn = sqlite3.connect(db)
c = conn.cursor()

def create_table():
    sql = 'CREATE TABLE IF NOT EXISTS ' + table_name + ' (ID INTEGER PRIMARY KEY AUTOINCREMENT, TaskName text)'
    c.execute(sql)

# How to Enter the Data
def data_entry(task):
    c.execute("INSERT INTO " + table_name + " (TaskName) VALUES (?)", [task])
    print("Task is added in database")
    conn.commit()

# How to print data
def printData():
    sql = "SELECT * FROM " + table_name
    c.execute(sql)
    for row in c.fetchall():
        print(row[0], "--->", row[1])
    

# How to delete the data
def deleteTask(index):
    c.execute("DELETE FROM " + table_name + " WHERE ID=?", (index, )) # adding a , after index makes it as a tuple
    print("Task deleted from database")

def deleteAll():
    c.execute("DELETE FROM " + table_name )
    print("All data deleted..")

# closing the Cursor()
def closeCursor():
    c.close()
    conn.close()

