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

class ModelYolo:
    def __init__(self):
        # self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='Lens_best.pt', source='local') # yolov5n - yolov5x6 or custom
        # CUDA 장치 설정
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        if device.type == 'cuda': 
            torch.cuda.set_device(0)  #원하는 GPU 장치 번호로 설정
        # 모델 로드
        self.model = torch.hub.load('./ultralytics/yolov5', 'custom', path='best_sss.pt', source='local')
        self.model.to(device)  # 모델을 GPU로 이동
    
class Client:
    # MAC Address
    def __init__(self, TCP_IP, TCP_PORT):
        self.__TCP_IP = TCP_IP
        self.__TCP_PORT = TCP_PORT
        self.__utility = Util()
        self.model = ModelYolo()
        self.connect()

    def connect(self) -> None:
        self.client_socket = socket.socket()
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

            self.resize_frame = cv2.resize(self.frame, dsize=(640, 640), interpolation=cv2.INTER_AREA)
            cv2.imshow('PC_cam', self.resize_frame)
            results = self.model.model(self.resize_frame)  # 수정됨
            # results.print()
            results.show()
            # DataFrame
            # print(results.pandas().xyxy[0][])
            # Series
            # print(results.pandas().xyxy[0].confidence.values)

            isFlag = False
            for value in results.pandas().xyxy[0].confidence.values:
                if value >= 0.6:
                    isFlag = True

            if isFlag:
                cam_img, cam_length = self.img_encoding(self.resize_frame)
                screen_shot, screen_shot_length = self.img_encoding(self.get_util().screen_shot())
                data, data_length = self.get_infomation()

                self.sendall(cam_img, cam_length)
                self.sendall(screen_shot, screen_shot_length)
                self.sendall(data, data_length)
                print('데이터를 보냈습니다...')
            

            # if results.pandas().xyxy[0].confidence >= 0.6:
            #     cam_img, cam_length = self.img_encoding(self.resize_frame)
            #     screen_shot, screen_shot_length = self.img_encoding(self.get_util().screen_shot())
            #     data, data_length = self.get_infomation()

            #     self.sendall(cam_img, cam_length)
            #     self.sendall(screen_shot, screen_shot_length)
            #     self.sendall(data, data_length)

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
        data = self.get_util().create_cominfo_to_json()
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
    
HOST = '192.168.50.187'
PORT = 9999

client = Client(HOST, PORT)