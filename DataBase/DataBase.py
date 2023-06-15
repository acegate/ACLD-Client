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


    def insertDepartment(self):
        sql = "INSERT INTO department(depmt_name, landline, location) VALUES(?, ?, ?)"
        part = ['경영지원', '영업', '기술', '생산', '총무', '경리', '구매', '인사', '자재', '홍보', '유통', '품질관리', '보수', '연구실', '인재개발', '국내판매', '해외판매', '개발']
        try:
            for i in range(1, len(part)+1):
                rnd_flow = random.choice(range(1, 6))
                rnd_ho = random.choice(range(1, 6))
                location = f'디지털 구로구 {rnd_flow}층 {rnd_flow}0{rnd_ho}호'
                rnd_name = random.choice(part)

                self.get_cursor().execute(sql,
                    (rnd_name, 5000+i, location)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)
        finally:
            self.close()

    def insertEmployee(self):
        sql = "INSERT INTO Employee(emp_no, depmt_no, emp_name, emp_img_path, phone_no, email, rank) VALUES(?, ?, ?, ?, ?, ?, ?)"
        names = ['박현주', '양승진', '이남일', '윤정자', '고원식', '황보원자', '성우현', '복기하', '김문옥', '신형우', '류범석', '고도현', '최수혁', '조윤혜', '양현우', '탁우재', '정상준', '권보경', '성정숙', '유해준']
        phones = []
        emails = []
        emp_img_path = 'C:/Users/user/media/'

        with open('./DataBase/phone_lists.txt', encoding='utf-8') as file:
            for line in file:
                phones.append(line)

        with open('./DataBase/random_emails.txt', encoding='utf-8') as file:
            for line in file:
                emails.append(line)

        emp_no = 1000
        try:
            for i in range(1000):
                depmt_no = random.choice(range(1, 19))
                emp_name = random.choice(names)
                phone_no = random.choice(phones)
                email = random.choice(emails)
                rnd_rank = random.choice(range(5))
                self.get_cursor().execute(sql, 
                (emp_no + i, depmt_no, emp_name, emp_img_path, phone_no, email, rnd_rank)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)
        finally:
            self.close()

    

    def insertIdentify(self):
        sql = "INSERT INTO identify(emp_no, agent_no, IP, MAC) VALUES(?, ?, ?, ?)"
        IPES = []
        with open('./DataBase/ip_range.txt', encoding='utf-8') as file:
            for line in file:
                IPES.append(line)
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


    def insertDetection(self):
        sql = "INSERT INTO dection(agent_no, CAM_path, screen_path, detectiontype, status) VALUES(?, ?, ?, ?, ?)"

        try:
            for i in range(10000):
                rnd_aget_no = random.choice(range(1, 1001))
                rnd_detectiontype = random.choice(range(2))
                rnd_status = random.choice(range(3))

                self.get_cursor().execute(sql,
                    (rnd_aget_no, 'C:/cam_img/', 'C:/screenshot/', rnd_detectiontype, rnd_status)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)
        finally:
            self.close()



    def insertAgent(self):
        sql = "INSERT INTO agent(status) VALUES(?)"

        try:
            for i in range(1000):
                status_no = random.choice(range(2))

                self.get_cursor().execute(sql,
                    (status_no, )
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)
        finally:
            self.close()

    def insertReport(self):
        sql = "INSERT INTO report(dect_no, content, status) VALUES(?, ?, ?)"
        contents = []

        with open('./DataBase/context.txt', encoding='utf-8') as file:
            for line in file:
                contents.append(line)
        try:
            for i in range(10000):
                rnd_dect_no = random.choice(range(1, 10001))
                rnd_content = random.choice(range(len(contents)))
                status = random.choice(range(3))
                self.get_cursor().execute(sql,
                    (rnd_dect_no, contents[rnd_content], status)
                )
                self.get_connection().commit()
        except Exception as e:
            print(f"Insert Error : {e}")
            sys.exit(1)
        finally:
            self.close()


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
database.insertReport()
