from GameClient import *
from time import *
from PyQt5.QtCore import *


class LoopThread(QThread,GameClient):
    update_signal = pyqtSignal(str)
    def __init__(self):
        GameClient.__init__(self)
        QThread.__init__(self)
        self.host = ''
        
    def run(self):
        while True:
            try:
                self.connect_to_server(self.host)
                break
            except:
                self.log("Exception: ")
                break
        self.play_loop()
        
    def play_loop(self):
        while True:
            msg_received = self.receive_message()
            if len(msg_received):
                self.update_signal.emit(str(msg_received))
            else:
                break
            
    def moves(self,messages):
        self.send_message(messages)



        #from GameClient import *
        #from time import *
        #from PyQt5.QtCore import *
        
        
        #class LoopThread(QThread,GameClient):
            #update_signal = pyqtSignal(str)
            #def __init__(self):
                #GameClient.__init__(self)
                #QThread.__init__(self)
                #self.host = ''
                
            #def run(self):
                #while True:
                    #msg_rec = self.receive_message()
                    #if len(msg_rec):
                        #self.update_signal.emit(str(msg_rec))
                    #else:
                        #break        
               
        
                    
            #def moves(self,messages):
                #self.socket.send(BUFFER_STR.format(messages).encode())
