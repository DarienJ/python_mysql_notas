import mysql.connector

#Conectar
def conectar(): 
    database=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database= "adsi",
        )
    cursor=database.cursor(buffered=True)

    return[database,cursor]
