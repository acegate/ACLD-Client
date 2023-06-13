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
        self.WINDOW_WIDTH = 720
        self.WINDOW_HEIGHT = 720
        self.X = window.winfo_screenwidth() // 2 - self.WINDOW_WIDTH // 2
        self.Y = window.winfo_screenheight() // 2 - self.WINDOW_HEIGHT // 2
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

    

    
