#!/usr/bin/python
import socket
import cv2
import numpy as np
import base64
import time
from datetime import datetime
import platform
import re, uuid
import json
from PIL import ImageGrab
import pyautogui
from tkinter import *




class Client:
    def __init__(self, TCP_IP, TCP_PORT):
        self.TCP_IP = TCP_IP
        self.TCP_PORT = TCP_PORT
        window = Tk()

        self.WINDOW_WIDTH = window.winfo_screenwidth()
        self.WINDOW_HEIGHT = window.winfo_screenheight()
        self.X = self.WINDOW_HEIGHT // 2
        self.Y = self.WINDOW_HEIGHT // 2
        
        self.create_computer_infomation()
        self.connect()


640 x 640
    def create_computer_infomation(self):
        info = platform.uname()
        cumputer_info = {
            'OS' : info[0],
            'userName' : socket.gethostname(),
            'CPU' : info[4],
            'MACAddress' : ':'.join(re.findall('..', '%012x'%uuid.getnode())),
        }
        self.infomation = json.dumps(cumputer_info)


    def connect(self):
        self.client_socket = socket.socket()
        self.client_socket.connect((self.TCP_IP, self.TCP_PORT))
        self.openCV()

    def openCV(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 315)


        while self.capture.isOpened():
            ret, self.frame = self.capture.read()
            if not ret:
                break

            self.resize_frame = cv2.resize(self.frame, dsize=(480,315), interpolation=cv2.INTER_AREA)
            encode_data = self.encoding(self.resize_frame)
            cam_length = str(len(encode_data))
            info_length = str(len(self.infomation))

            cv2.imshow('PC_cam', self.resize_frame)


            if cv2.waitKey(1) == ord('q'):
                pic = pyautogui.screenshot(region=(self.X, self.Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
                img_frame = np.array(pic)
                encode_picture = self.encoding(img_frame)
                picture_length = str(len(encode_picture))
                print(picture_length)

                stime = datetime.utcnow().strftime("%Y/%m/%D %H:%M:%S.%f")

                self.send(cam_length, encode_data)
                self.client_socket.send(stime.encode('utf-8').ljust(64))
                self.send(info_length, self.infomation.encode('utf-8'))
                # break

            time.sleep(0.095)
        
        self.client_socket.close()
        self.capture.release()
        cv2.destroyAllWindows()
        
    def send(self, length, data):
        self.client_socket.sendall(length.encode('utf-8').ljust(64))
        self.client_socket.send(data)

    def encoding(self, image_frame):
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
        result, imgencode = cv2.imencode('.jpg', image_frame, encode_param)
        data = np.array(imgencode)
        StringData = base64.b64encode(data)
        return StringData
    
    def window_screen_shot(self):
        img = ImageGrab.grab()
        imgCrop = img.crop((self.X, self.Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        saveas = f"{'windowscreen'}{'.png'}"
        # imgCrop.save(saveas)
        return saveas


HOST = '192.168.50.129'
PORT = 9999

client = Client(HOST, PORT)