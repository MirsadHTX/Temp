import mysql.connector
import pyOpenSSL


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Nijevazno1",
  auth_plugin='sha256_password'
)

print(mydb)