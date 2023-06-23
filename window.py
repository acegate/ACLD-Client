from tkinter import *
from client_image import Client
import threading

SABORN = '23051489'
host = '192.168.50.131'
port = '9999'

class Window:
    def __init__(self):
        self.__window = Tk()
        self.__WINDOW_WIDTH = 200
        self.__WINDOW_HEIGHT = 100
        self.__X = self.get_window().winfo_screenwidth() // 2 - self.get_width() // 2
        self.__Y = self.get_window().winfo_screenheight() // 2 - self.get_height() // 2
        self.create()
        self.attachForm()
        self.get_window().mainloop() 
    
    def create(self):
        self.get_window().title('Client')
        self.get_window().geometry(f'{self.get_width()}x{self.get_height()}+{self.get_X()}+{self.get_Y()}')
        self.get_window().resizable(False, False)

    def attachForm(self):
        sabon_label = Label(self.get_window(), text='사번').grid(row=0, column=0)
        host_label = Label(self.get_window(), text='HOST').grid(row=1,column=0)
        port_label = Label(self.get_window(), text='포트').grid(row=2, column=0)

        self.saborn_input_text = Entry(self.get_window())
        self.get_saborn_input_text().grid(row=0,column=1)
        self.get_saborn_input_text().insert(END, SABORN)

        self.host_input_text = Entry(self.get_window())
        self.get_host_input_text().grid(row=1,column=1)
        self.get_host_input_text().insert(END, host)

        self.port_input_text = Entry(self.get_window())
        self.get_port_input_text().grid(row=2,column=1)
        self.get_port_input_text().insert(END, port)

        button = Button(self.get_window(), text='로그인',bg='blue', width=10, fg='white', command=self.clicked).grid(row=3,column=1)

    def clicked(self):
        saborn = self.get_saborn_input_text().get()
        HOST = self.get_host_input_text().get()
        PORT = self.get_port_input_text().get()

        thread = threading.Thread(target=Client, args=(HOST, int(PORT), saborn))
        thread.start()
        # self.get_window().destroy()


    def get_port_input_text(self):
        return self.port_input_text

    def get_saborn_input_text(self):
        return self.saborn_input_text
    
    def get_host_input_text(self):
        return self.host_input_text

    def get_window(self):
        return self.__window
    
    def get_width(self):
        return self.__WINDOW_WIDTH
    
    def get_height(self):
        return self.__WINDOW_HEIGHT
    
    def get_X(self):
        return self.__X
    
    def get_Y(self):
        return self.__Y



window = Window()
