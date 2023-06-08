#!/usr/bin/python
import socket
import cv2
import numpy as np
import base64
import time
from datetime import datetime
from tkinter import *
from util import Util

class Client:
    # MAC Address
    def __init__(self, TCP_IP, TCP_PORT):
        self.TCP_IP = TCP_IP
        self.TCP_PORT = TCP_PORT
        self.utility = Util()
        self.connect()

    def connect(self) -> None:
        self.client_socket = socket.socket()
        self.client_socket.connect((self.TCP_IP, self.TCP_PORT))
        self.openCV()

    def openCV(self) -> None:
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

        while self.capture.isOpened():
            ret, self.frame = self.capture.read()
            if not ret:
                break

            self.resize_frame = cv2.resize(self.frame, dsize=(640, 640), interpolation=cv2.INTER_AREA)
            cv2.imshow('PC_cam', self.resize_frame)

            if cv2.waitKey(1) == ord('q'):
                cam_img = self.cam_img_encoding(self.resize_frame)
                screen_shot = self.window_screen_shot()
                nowtime = self.get_time()
                
                # self.utility.create_img(self.resize_frame, self.CAM_IMG_FLAG)
                # self.utility.create_img(self.screen_shot, self.SCREENSHOT_FLAG)
                # self.utility.transfer_zip()
                self.send_recive(screen_shot)
                # self.send_recive(cam_img)
                # self.send_recive(nowtime)

                # print(encode_cam_img)
                # print(nowtime)
                # self.send_recive(screen_shot[0], screen_shot[1])
                # self.send_recive(encode_cam_img[0], encode_cam_img[1])
                # self.send_recive(nowtime[0], nowtime[1])
                # self.send_recive(self.computer_info_length, self.computer_info)

                # break

            time.sleep(0.095)
        
        self.client_socket.close()
        self.capture.release()
        cv2.destroyAllWindows()
        
    def send_recive(self, data) -> None:
        # self.client_socket.sendall(length.encode('utf-8').ljust(64))
        self.client_socket.sendall(data)


    def get_time(self) -> tuple:
        nowtime = datetime.utcnow().strftime("%Y/%m/%D %H:%M:%S.%f")
        # nowtime_length = str(len(nowtime))
        return nowtime

    def cam_img_encoding(self, image_frame) -> tuple:
        encode_param=[int(cv2.IMWRITE_JPEG_QUALITY), 60]
        result, imgencode = cv2.imencode('.png', image_frame, encode_param)
        data = np.array(image_frame)
        img_to_byte = base64.b64encode(data)
        # cam_img_length = str(len(string_data))
        return img_to_byte
    
    def window_screen_shot(self) -> tuple:
        img = np.array(self.utility.screen_shot())
        data = np.array(img)
        img_to_byte = base64.b64encode(data)
        # screen_shot_length = str(len(string_data))
        return img_to_byte
    
HOST = '192.168.101.1'
PORT = 9999

client = Client(HOST, PORT)