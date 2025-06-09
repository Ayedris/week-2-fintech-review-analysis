
import oracledb
#print("OracleDB module is working!")

connection = oracledb.connect(
   user="System", 
   password="Omebank66127", 
    dsn="127.0.0.1:1521/freepdb1"
)
print("Connected successfully!")
connection.close()