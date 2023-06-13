import mariadb
import sys
import random
from datetime import datetime
import time
import pandas as pd

class DataBase:
    def __init__(self, user_name, user_pwd, HOST, PORT, db_name):
        sql = "INSERT INTO Employee(employee_no, part_no_FK, name, employee_img_path, email, phone_number, rank, address, join_day) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"

        try:
            conn = mariadb.connect(
                user=user_name,
                password=user_pwd,
                host=HOST,
                port=PORT,
                database=db_name
            )
            cur = conn.cursor()
            names = ['이순신', '홍길동', '유경달', '안미채', '어판미', '나뜸수', '원민문']

            for i in range(1000):
                part_no = random.choice(range(1, 9))
                phone_no = random.choice(range(1, 10))
                rank_no = random.choice(range(1, 5))
                name = random.choice(names)

                phone_no = random.choice(range(1, 10))
                phone_number = f'010{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}{phone_no}'

                cur.execute(sql, 
                    (6666777+i, part_no, name, 'C:/Users/user/Desktop/Client', 'test@gmail.com', int(phone_number), rank_no, '서울시 강변로 테스트리 202-10 303동 3003호', datetime.now())
                )
                time.sleep(4)

        except Exception as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)


user_name = 'root'
user_pwd = '1735'
HOST = '192.168.50.131'
PORT = 3306
db_name = 'company'

database = DataBase(user_name, user_pwd, HOST, PORT, db_name)