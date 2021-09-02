import sqlite3   

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE routine (id INTEGER PRIMARY KEY, date text , earnings integer , excercise text , study text , diet text , python integer)")
    conn.commit()
    conn.close()

def insert(date , earnings , excercise , study, diet, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ? , ? , ? , ? , ? , ?)" , (date, earnings, excercise, study, diet, python))
    conn.commit()
    conn.close()


insert('1-2-2019',200, 'no excercise', 'no study', 'diet taken' , 'did python')