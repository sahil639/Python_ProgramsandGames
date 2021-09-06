import sqlite3   

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS routine (id INTEGER PRIMARY KEY, date text , earnings integer , excercise text , study text , diet text , python integer)")
    conn.commit()
    conn.close()

def insert(date , earnings , excercise , study, diet, python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL , ? , ? , ? , ? , ? , ?)" , (date, earnings, excercise, study, diet, python))
    conn.commit()
    conn.close()



def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine" )
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id = ? ", (id,))
    conn.commit()
    conn.close()

def search(date='' , earnings='' , excercise='' , study='', diet='', python=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR excercise=? OR study=? OR diet=? OR python=?", (date , earnings , excercise , study, diet, python))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
    
connect()
# insert('2-2-2019',200, 'no excercise', 'no study', 'diet taken' , 'did python')