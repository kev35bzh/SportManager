from threading import Thread
from data import *
from server import *
from interface import *

# Thread declaration
thread_udp = UdpCommunication(data_udp)
thread_interface = DisplayManager(data_udp)

# Thread start
thread_udp.start()   
thread_interface.mainloop()
  
# Thread Stop     
del thread_udp
del thread_interface