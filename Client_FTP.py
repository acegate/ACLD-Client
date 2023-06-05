import ftplib
import os
from datetime import datetime
from PIL import ImageGrab
import cv2
import numpy as np

class Client_FTP:
  def __init__(self):
    self.HOST = '192.168.50.129'
    self.USER = 'FTP_user'
    self.PASSWORD = '1735'
    self.YEAR = datetime.now().year
    self.MONTH = '%02d' % datetime.now().month
    self.DAY = '%02d' % datetime.now().day
    self.trans_str = list(map(str, [self.YEAR, self.MONTH, self.DAY]))
    self.ROOT_PATH = f'./{self.trans_str[0]}/{self.trans_str[1]}/{self.trans_str[2]}'
    self.connect()
    self.X = 0
    self.Y = 0
    self.WINDOW_WIDTH = 1920
    self.WINDOW_HEIGHT = 1080

  def window_screen_shot(self):
      img = ImageGrab.grab()
      imgCrop = img.crop((self.X, self.Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
      saveas = f"{'windowscreen'}{'.png'}"
      imgCrop.save(saveas)

  def connect(self):
    try:
      with ftplib.FTP() as ftp:
        ftp.connect(host=self.HOST,port=21)
        ftp.encoding = 'utf-8'
        session = ftp.login(user=self.USER, passwd=self.PASSWORD)

        list = os.listdir(self.ROOT_PATH)

        ftp.mkd('/test1/test2/test3')

        # for file in list :
            # if file != '다운로드 - 복사본.zip':
              # continue
            # with open(file=self.ROOT_PATH + f'/{file}', mode='rb') as f:
              # pass
                # ftp.storbinary(f'STOR {self.YEAR}{self.MONTH}{self.DAY}.zip', f)
              
        print(ftp.dir())

        ftp.quit()
    
    except Exception as e:
      print(e)



test = Client_FTP()