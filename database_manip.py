import sqlite3
db = sqlite3.connect('data/python_programming')
cursor = db.cursor()

# Creating a table with the following headers: id, name, grade.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS python_programming
        (id INTEGER PRIMARY KEY NOT NULL, name TEXT,
        grade INTEGER)
''')
db.commit()

# Below data will be added to the table (database).
cursor = db.cursor() 
id1 = 55
name1 = 'Carl Davies'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peython Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# All data will be added at the same time due to using 'executemany'.
students_data = [(id1,name1,grade1), (id2,name2,grade2), (id3,name3,grade3), (id4,name4,grade4), (id5,name5,grade5)]
cursor.executemany('''INSERT or REPLACE INTO python_programming(id,name,grade) VALUES(?,?,?)''', (students_data))
print('USERS inserted')
db.commit()

#All records with grade between 60 and 80 is selected
cursor.execute('''SELECT id,name,grade FROM python_programming WHERE id BETWEEN 60 and 80''')
python_programming = cursor.fetchall()
print("Data fetched")

#Carl Davis grade is changed to 65.
grade = 65
name = 'Carl Davies'
cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ?''', (grade, name))
print("Student grade updated")

# Dennis Fredrickson is removed from the database
name = 'Dennis Fredrickson'
cursor.execute('''DELETE FROM python_programming WHERE name = ?''', (name,))
print("Student deleted")

#All people with id below 55 have their grade changed to 25.
grade = 25
cursor.execute('''UPDATE python_programming SET grade = ? WHERE id<55''', (grade,))
print("grades updated")

db.commit()
db.close()
print('Connection to database closed')
