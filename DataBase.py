
import mariadb
import sys



class DataBase:
    def __init__(self, user_name, user_pwd, HOST, PORT, db_name):
        try:
            conn = mariadb.connect(
                user=user_name,
                password=user_pwd,
                host=HOST,
                port=PORT,
                database=db_name
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        self.cur = conn.cursor()



user_name = 'root'
user_pwd = '1735'
HOST = '192.168.50.131'
PORT = 3306
db_name = 'acdd'



database = DataBase(user_name, user_pwd, HOST, PORT, db_name)
