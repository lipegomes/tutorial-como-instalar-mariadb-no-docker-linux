from getpass import getpass
from mysql.connector import connect, Error

# Conectar a base de dados existente no MariaDB
try:
    with connect(
        host="localhost",
        user=input("Digite o username: "),
        password=getpass("Digite o  password: "),
        # Base de dados
        database="TUTORIAL_MARIADB",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

# O código acima retonar a conexão em forma de objeto:
# <mysql.connector.connection_cext.CMySQLConnection object at 0x7fd15f9df220>
