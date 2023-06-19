#!/usr/bin/python
import socket
import cv2
import numpy as np
import base64
import time
from datetime import datetime
from tkinter import *
from util import Util
import json
import torch
from model import ModelYolo

    
class Client:
    # MAC Address
    def __init__(self, TCP_IP, TCP_PORT, saborn):
        self.__saborn = saborn
        self.__TCP_IP = TCP_IP
        self.__TCP_PORT = TCP_PORT
        self.__utility = Util()
        self.model = ModelYolo()
        self.connect()

    def connect(self) -> None:

        self.client_socket = socket.socket()
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 1)
        self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 3)
        self.client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 1)
        
        self.client_socket.connect((self.get_host(), self.get_port()))
        self.openCV()

    def openCV(self) -> None:
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

        while self.capture.isOpened():
            ret, self.frame = self.capture.read()
            if not ret:
                break

            self.resize_frame = cv2.resize(self.frame, dsize=(640, 640), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('PC_cam', self.resize_frame)
            results = self.model.model(self.resize_frame)  # 수정됨
            # results.print()
            results.show()
            # DataFrame
            # print(results.pandas().xyxy[0][])
            # Series
            # print(results.pandas().xyxy[0].confidence.values)

            if results.pandas().xyxy[0].confidence >= 0.6:
                cam_img, cam_length = self.img_encoding(self.resize_frame)
                screen_shot, screen_shot_length = self.img_encoding(self.get_util().screen_shot())
                data, data_length = self.get_infomation()

                self.sendall(cam_img, cam_length)
                self.sendall(screen_shot, screen_shot_length)
                self.sendall(data, data_length)

            time.sleep(1)
        
        self.client_socket.close()
        self.capture.release()
        cv2.destroyAllWindows()
        
    def sendall(self, data, length) -> None:
        self.client_socket.sendall(length.encode('utf-8').ljust(64))
        self.client_socket.send(data)


    def img_encoding(self, image_frame) -> tuple:
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 60]
        result, imgencode = cv2.imencode('.jpg', image_frame, encode_param)
        data = np.array(imgencode)
        img_to_byte = base64.b64encode(data)
        cam_img_length = str(len(img_to_byte))
        return (img_to_byte, cam_img_length)
    

    def get_infomation(self) -> tuple:
        data = self.get_util().create_infomation(self.get_saborn())
        data['datetime'] = self.get_time()
        to_json_data = json.dumps(data).encode('utf-8')
        data_length = str(len(to_json_data))
        return (to_json_data, data_length)
    
    def get_time(self) -> tuple:
        return datetime.utcnow().strftime("%Y/%m/%D %H:%M:%S")
   
    def get_util(self):
        return self.__utility
    
    def get_host(self):
        return self.__TCP_IP
    
    def get_port(self):
        return self.__TCP_PORT
    


