from tkinter import *
from .client_image import Client

class Window:
    def __init__(self, HOST, PORT):
        self.__HOST = HOST
        self.__PORT = PORT
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

        self.sabon_input_text = Entry(self.get_window())
        self.get_sabon_input_text().grid(row=0,column=1)

        self.host_input_text = Entry(self.get_window())
        self.get_host_input_text().grid(row=1,column=1)
        self.get_host_input_text().insert(END, self.get_host())

        self.port_input_text = Entry(self.get_window())
        self.get_port_input_text().grid(row=2,column=1)
        self.get_port_input_text().insert(END, self.get_port())

        button = Button(self.get_window(), text='등록',bg='blue', width=10, fg='white', command=self.clicked).grid(row=3,column=1)

    def clicked(self):
        sabon = self.get_sabon_input_text().get()
        HOST = self.get_host_input_text().get()
        PORT = self.get_port_input_text().get()
        client = Client(HOST, PORT)



    def get_port_input_text(self):
        return self.port_input_text

    def get_sabon_input_text(self):
        return self.sabon_input_text
    
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
    
    def get_host(self):
        return self.__HOST
    
    def get_port(self):
        return self.__PORT

HOST = '192.168.50.187'
PORT = 9999
window = Window(HOST, PORT)