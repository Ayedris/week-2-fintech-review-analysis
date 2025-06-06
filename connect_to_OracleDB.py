
import oracledb
#print("OracleDB module is working!")

connection = oracledb.connect(
   user="System", 
   password="O@mebank66127", 
    dsn="127.0.0.1:1521/freepdb1"
)
print("Connected successfully!")
connection.close()