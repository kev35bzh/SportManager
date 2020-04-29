import socket
import time
from threading import Thread
from data import *
import pickle



class UdpCommunication(Thread): 
    """Thread managing udp commmunication"""
         
    def __init__(self,data_udp): 
        """ Constructor initialize udp communication """       
        Thread.__init__(self)
        self.udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_server_socket.connect((hote, port))
        self.data_udp=data_udp

    def run(self):
        while(True):
            stream = pickle.dumps(self.data_udp)
            self.udp_server_socket.send(stream) 
            time.sleep(1)    
        
    def __del__(self):
        """ Destructor close udp communication """
        self.udp_server_socket.close()   