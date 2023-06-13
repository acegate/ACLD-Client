import mariadb
import sys
import random
from datetime import datetime
import time
import pandas as pd

class DataBase:
    def __init__(self, user_name, user_pwd, HOST, PORT, db_name):
        try:
            self.__conn = mariadb.connect(
                user=user_name,
                password=user_pwd,
                host=HOST,
                port=PORT,
                database=db_name
            )
        except Exception as e:
            print(f'Connection Error : {e}')
            sys.exit(1)

    def insert_dummy(self):
        sql = "INSERT INTO Employee(employee_no, part_no_FK, name, employee_img_path, email, phone_number, rank, address, join_day) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        names = ['이순신', '홍길동', '유경달', '안미채', '어판미', '나뜸수', '원민문']
        self.count = 1000

        for i in range(1000):
            self.part_no = random.choice(range(1, 9))
            phone_no = random.choice(range(1, 10))
            self.rank_no = random.choice(range(1, 5))
            self.name = random.choice(names)
            phone_no = random.choice(range(1, 10))
            self.phone_number = f'010{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}'
            self.insert(sql)
            self.count += 1 

    def insert(self, sql):
        try:
            self.get_cursor().execute(sql, 
                (self.count, self.part_no, self.name, 'C:/Users/user/Desktop/Client', 'test@gmail.com', self.phone_number, self.rank_no, '서울시 강변로 202-10 303동 3003호', datetime.now())
            )
            self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)
        

    def select_dummy(self, sabon):
        self.sabon = sabon
        sql = "SELECT * FROM employee into outfile './result.csv' fields terminated by ','"
        self.select(sql)

    def select(self, sql):
        try:
            self.get_cursor().execute(sql)

            self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)


    def get_cursor(self):
        try:
            cur = self.get_connection().cursor()
        except Exception as e:
            print('get cursor Error')
        return cur
    

    def close(self):
        self.get_cursor().close()
        self.get_connection().close()
    
    def get_connection(self):
        return self.__conn



user_name = 'root'
user_pwd = '1735'
HOST = '192.168.50.131'
PORT = 3306
db_name = 'company'

database = DataBase(user_name, user_pwd, HOST, PORT, db_name)

database.select_dummy(6666777)
# database.insert_dummy()