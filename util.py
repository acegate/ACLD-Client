import os
from datetime import datetime
import platform
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

    def create_cominfo_to_json(self) -> dict:
        info = platform.uname()
        temp = {
            'IP' : socket.gethostname(),
            'userName' : info[1],
            'MACAddress' : ':'.join(re.findall('..', '%012x'%uuid.getnode())),
        }
        return temp

    def screen_shot(self) -> Image:
        return pyautogui.screenshot(region=(self.X, self.Y, self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        

    def get_rootpath(self):
        return self.__path
    
    def get_computer_info(self):
        return self.__computer_info

    

    
