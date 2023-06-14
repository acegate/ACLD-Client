import mariadb
import sys
import random
from datetime import datetime, timedelta
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

    def insertEmployee(self):
        sql = "INSERT INTO Employee(emp_no, workdept, emp_name, emp_img_path, phone_no, email, address, gender, rank, hiredate) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        names = ['박현주', '양승진', '이남일', '윤정자', '고원식', '황보원자', '성우현', '복기하', '김문옥', '신형우', '류범석', '고도현', '최수혁', '조윤혜', '양현우', '탁우재', '정상준', '권보경', '성정숙', '유해준']
        phones = []
        emails = []
        addresses = []
        local_path = 'C:/Users/user/Searches/'
        timestamps = []

        with open('./DataBase/phone_lists.txt', encoding='utf-8') as file:
            for line in file:
                phones.append(line)

        with open('./DataBase/random_emails.txt', encoding='utf-8') as file:
            for line in file:
                emails.append(line)

        with open('./DataBase/random_addresses.txt', encoding='utf-8') as file:
            for line in file:
                addresses.append(line)

        with open('./DataBase/random_hire_dates.txt', encoding='utf-8') as file:
            for line in file:
               timestamps.append(line)
        timestamps = list(map(int, timestamps))

        count = 1000
        for i in range(1000):
            part_no = random.choice(range(2, 20))
            phone_no = random.choice(range(1, 10))
            rank_no = random.choice(range(1, 7))
            name = random.choice(names)
            email = random.choice(emails)
            phone_no = random.choice(phones)
            address = random.choice(addresses)
            gender = random.choice(['M', 'F'])
            timestamp = random.choice(timestamps)

            try:
                self.get_cursor().execute(sql, 
                (count + i, part_no, name, local_path, phone_no, email, address, gender, rank_no, datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))
                )
                self.get_connection().commit()
            except Exception as e:
                print(f"Insert Error : {e}")
                sys.exit(1)





    def insertAddress(self):
        sql = "INSERT INTO location(loc_name) VALUES(?)"

        address = [
            '경기도 남양주시 화도읍 가구단지중앙길 13-8 12178', '경기도 부천시 범박로 16-8(범박동) 14783',
            '경상남도 밀양시 멍에실로 63-18(가곡동) 50446' , '경상남도 양산시 상북면 충렬로 1123-99 50579',
        ]

        try:
            for i in range(1, 6):
                rnd_address = random.choice(address)

                self.get_cursor().execute(sql,
                        (rnd_address, )
                )
                self.get_connection().commit()
            
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)

    def insertDepartment(self):
        sql = "INSERT INTO department(location, depmt_name, landline) VALUES(?, ?, ?)"
        part = ['경영지원', '영업', '기술', '생산', '총무', '경리', '구매', '인사', '자재', '홍보', '유통', '품질관리', '보수', '연구실', '인재개발', '국내판매', '해외판매', '개발']
        try:
            for i in range(1, len(part)+1):
                rand_location = random.choice(range(1, 6))

                self.get_cursor().execute(sql,
                    (rand_location, part[i-1], 5000+i)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)

    def insertLog(self):
        sql = "INSERT INTO log(agent_no_FK, CAM_path, screen_path, detectiontype, status) VALUES(?, ?, ?, ?, ?)"

        try:
            for i in range(10000):
                rand_agent_no = random.choice(range(1, 1001))
                rand_detectiontype = random.choice(range(3))
                rand_status = random.choice(range(3))

                self.get_cursor().execute(sql,
                    (rand_agent_no, 'C:/cam_img/', 'C:/screenshot/', rand_detectiontype, rand_status)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)



    def insertAgent(self):
        sql = "INSERT INTO agent(emp_no_FK, MAC_Address, IP, agent_number) VALUES(?, ?, ?, ?)"
        mac_addresses = []
        ipes = []

        with open('./DataBase/random_macaddress.txt', encoding='utf-8') as file:
            for line in file:
                mac_addresses.append(line)

        with open('./DataBase/random_ip_addresses.txt', encoding='utf-8') as file:
            for line in file:
                ipes.append(line)

        try:
            for i in range(1, 1001):
                rnd_emp_no = range(1000, 2000)
                rnd_mac = random.choice(mac_addresses)
                rnd_ip = random.choice(ipes)

                self.get_cursor().execute(sql,
                    (rnd_emp_no[i-1], rnd_mac, rnd_ip, i)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)

    def insertReport(self):
        sql = "INSERT INTO report(log_no_FK, content, status) VALUES(?, ?, ?)"
        contents = []

        with open('./DataBase/context.txt', encoding='utf-8') as file:
            for line in file:
                contents.append(line)
        try:
            for i in range(10000):
                rnd_log_no = random.choice(range(1, 10001))
                rnd_content = random.choice(range(len(contents)))
                status = random.choice(range(3))
                self.get_cursor().execute(sql,
                    (rnd_log_no, contents[rnd_content], status)
                )
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
db_name = 'acdd'

database = DataBase(user_name, user_pwd, HOST, PORT, db_name)

# database.insertAddress()
# database.insertDepartment()
# database.insertEmployee()

# database.insertAgent()
# database.insertLog()
database.insertReport()


