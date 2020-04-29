from tkinter import *
from data import *
import time
from _ctypes import alignment

class DisplayManager(Tk):
    """ Class managing interface """
 
    def __init__(self,data_udp):
        """ Constructor initialize interface """
        self.display = Tk.__init__(self)
        self.data_udp=data_udp
        self.title("Sport Manager")
        self.display_frame = Frame(self.display)
        self.name_team1="Enter Name"
        self.name_team2="Enter Name"
        self.state_chrono="OFF"
        
        # Create Object
        self.label_team1 = Label(self.display_frame, text="Team1", anchor='e')  
        self.label_team2 = Label(self.display_frame, text="Team2", anchor='e')
        self.label_timeout = Label(self.display_frame, text="Timeout", anchor='e')  
        self.entry_team1 = Entry(self.display_frame, width=10)#, text=self.name_team1)
        self.entry_team2 = Entry(self.display_frame,width=10)#, text=self.name_team2)  
        self.chrono = Button(self.display_frame, text="OFF",command=self.timeout, bg='red')
      
        # Dispach object on frame
        self.label_team1.grid(row=2, column=1, ipadx=1, ipady=1, padx=10, pady=5)
        self.label_team2.grid(row=4, column=1, ipadx=1, ipady=1, padx=10, pady=5)
        self.label_timeout.grid(row=6, column=1, ipadx=1, ipady=1, padx=5, pady=5)
        self.entry_team1.grid(row=2, column=2, ipadx=10, ipady=1, padx=20, pady=5)
        self.entry_team2.grid(row=4, column=2, ipadx=10, ipady=1, padx=20, pady=5)
        self.chrono.grid(row=6, column=2, ipadx=1, ipady=1, padx=20, pady=5)
        
        self.display_frame.pack()
        self.update()
        
    def timeout(self):
        if self.chrono['text']=='OFF':
            self.chrono['text']='ON'
            self.chrono['bg']='green'
        else:
            self.chrono['text']='OFF'
            self.chrono['bg']='red'

    def update(self):
        self.name_team1=self.entry_team1.get()
        self.name_team2=self.entry_team2.get()
        self.state_chrono=self.chrono['text']
        self.data_udp[0]=self.name_team1
        self.data_udp[1]=self.name_team2
        self.data_udp[2]=self.state_chrono
        self.after(1000, self.update)
        
    def __del__(self):
        """ Destructor interface """          