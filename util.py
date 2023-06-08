import os
from datetime import datetime
import platform
import json
import re, uuid
import socket
from tkinter import *
import pyautogui

class Util:
    def __init__(self):
        window = Tk()
        self.X = 0
        self.Y = 0
        self.WINDOW_WIDTH = window.winfo_screenwidth()
        self.WINDOW_HEIGHT = window.winfo_screenheight()
        self.create_cominfo_to_json()

    def create_cominfo_to_json(self) -> None:
        info = platform.uname()
        temp = {
            'OS' : info[0],
            'IP' : socket.gethostname(),
            'userName' : info[1],
            'MACAddress' : ':'.join(re.findall('..', '%012x'%uuid.getnode())),
        }
        self.__computer_info = json.dumps(temp)
        # self.computer_info_length = str(len(self.computer_info))

    def screen_shot(self):
        screen_shot = pyautogui.screenshot(region=(self.X, self.Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        return screen_shot

    def get_rootpath(self):
        return self.__path
    
    def get_computer_info(self):
        return self.__computer_info

    

    
