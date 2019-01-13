import sqlite3

dBObject = sqlite3.connect("..\ZZDataFiles\MirsadDataBase.db")

cur = dBObject.cursor()

#cur.execute(""" CREATE TABLE elever (Navn text, Efternavn text, Opgave integer, Vurdering integer)""")
#cur.execute(" INSERT INTO elever VALUES('Mirsad', 'Kadribasic', 16, 1)")
#dBObject.commit()

cur.execute("SELECT * FROM elever WHERE Opgave='16'")

print(cur.fetchall())