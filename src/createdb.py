from getpass import getpass
from mysql.connector import connect, Error

# Estabece conexão com o MariaDB
try:
    with connect(
        host="localhost",
        # username = root
        user=input("Digite o username: "),
        # password = @#dev2021
        password=getpass("Digite o password: "),
    ) as connection:
        create_db_query = "CREATE DATABASE TUTORIAL_MARIADB"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
