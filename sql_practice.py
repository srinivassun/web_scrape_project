import sqlite3

#Establish a connection and cursor
connection = sqlite3.Connection("data.db")
cursor = connection.cursor()

#Query data using cursor
cursor.execute("select * from events")
print(cursor.fetchall())

#Insert a new row
insert = "insert into events values('Tigers','LosAngles City','2077.10.22')"
cursor.execute(insert)
connection.commit()

#Insert multiple rows
rows = [('Cats','Cat City','2066.12.13'),
        ('Hens','Hen City','2055.12.14')]
cursor.executemany("insert into events values(?,?,?)",rows)
connection.commit()