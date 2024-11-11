import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import random
from GameClient import*
from PyQt5.QtCore import *
from LoopThread import *



class OXOGame(QWidget, GameClient): 
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        GameClient.__init__(self)# Constructor
        self.setWindowTitle('OXO GAME') #Setting a windows
        self.setMaximumSize(1000,1000)# set the window size
        self.setWindowIcon(QIcon("combo")) # set icon window
        
        #Setting a heading
        self.welcome = QLabel("WELCOME TO THE WORLD OF \n___________________________________________")
        self.welcome.setFont(QFont('Times',20, QFont.Bold)) #Enlarging the label and writing it bold
        self.pixmap = QPixmap('nought') #Setting a picture
        self.pic_image = QLabel(self)
        self.pic_image.setPixmap(self.pixmap.scaled(100, 50))
        self.pixmap = QPixmap('cross') #Setting a picture
        self.pic_lab = QLabel(self)
        self.pic_lab.setPixmap(self.pixmap.scaled(100, 50))
        self.pixmap = QPixmap('nought') #Setting a picture
        self.pic_sthombe = QLabel(self)
        self.pic_sthombe.setPixmap(self.pixmap.scaled(100, 50)) 
        
        #Setting my shape
        self.pixmap = QPixmap("blank") #Setting a picture
        self.pic_label = QLabel(self)
        self.pic_label.setPixmap(self.pixmap.scaled(100, 100))
        
        #Setting a background initial colour
        self.setPalette(QPalette(QColor('magenta')))        
        
        #create labels
        label = QLabel("Enter server:")
        label.setFont(QFont('Times',16,3)) #Enlarging the label
        messages_label =QLabel("<<<<<<Messages from server>>>>>>")
        messages_label.setFont(QFont('Times',16,3))#Enlarging the label
        Game_label = QLabel("<<<<<<<The Game>>>>>>>")
        Game_label.setFont(QFont('Times',16,3))#Enlarging the label
        Shape_label =QLabel("<My shape>")
        Shape_label.setFont(QFont('Times',16,3))#Enlarging the label
        
        #create line edits
        self.label_edit =QLineEdit()
        self.label_edit.setPlaceholderText("Enter server name")
        self.label_edit.setFont(QFont('Times',16,3))#Enlarging the placeholder
        self.messages_edit =QTextEdit()
        self.messages_edit.setFixedSize(400, 200)#Sizing the message box
        self.messages_edit.setFont(QFont('Times',16,3))#Enlarging messages that display in message edit
    
        #Create buttons
        self.connect_button =QPushButton("Connect")
        self.connect_button.setFont(QFont('Times',16,3))#Enlarging the button
        self.Quit_button =QPushButton("Quit")
        self.Quit_button.setFont(QFont('Times',16,3))#Enlarging the button
        
        self.instruction_button = QPushButton("Instructions")
        self.instruction_button.setFont(QFont('Times',16,3))#Enlarging the button
        self.instruction_button.clicked.connect(self.information)#Connecting the instruction button
        
        # list for storing the buttons
        self.Buttons = []
        
        #create buttons
        self.button1 = QToolButton()
        self.button1.setFixedSize(100, 100) #Enlarging the button
        self.button1.setIconSize(self.button1.size())# Setting the picture in the button
        self.Buttons.append(self.button1) # appending the button to the list
        self.button1.clicked.connect(self.button1_clicked)# connecting button to a method
        
        self.button2 = QToolButton()
        self.button2.setFixedSize(100, 100) #Enlarging the button
        self.button2.setIconSize(self.button2.size())# Setting the picture in the button
        self.Buttons.append(self.button2)# appending the button to the list
        self.button2.clicked.connect(self.button2_clicked)# connecting button to a method
        
        self.button3 = QToolButton()
        self.button3.setFixedSize(100, 100) #Enlarging the button
        self.button3.setIconSize(self.button3.size())# Setting the picture in the button
        self.Buttons.append(self.button3)# appending the button to the list
        self.button3.clicked.connect(self.button3_clicked)# connecting button to a method
        
        self.button4 = QToolButton()
        self.button4.setFixedSize(100, 100) #Enlarging the button
        self. button4.setIconSize(self.button4.size())# Setting the picture in the button
        self.Buttons.append(self.button4)# appending the button to the list
        self.button4.clicked.connect(self.button4_clicked)# connecting button to a method
        
        self.button5 = QToolButton()
        self.button5.setFixedSize(100, 100) #Enlarging the button
        self.button5.setIconSize(self.button5.size())# Setting the picture in the button
        self.Buttons.append(self.button5)# appending the button to the list
        self.button5.clicked.connect(self.button5_clicked)# connecting button to a method
        
        self.button6 = QToolButton()
        self.button6.setFixedSize(100, 100) #Enlarging the button
        self.button6.setIconSize(self.button6.size())# Setting the picture in the button
        self.Buttons.append(self.button6)# appending the button to the list
        self.button6.clicked.connect(self.button6_clicked)# connecting button to a method
        
        self.button7 = QToolButton()
        self.button7.setFixedSize(100, 100) #Enlarging the button
        self.button7.setIconSize(self.button7.size())# Setting the picture in the button
        self.Buttons.append(self.button7)# appending the button to the list
        self.button7.clicked.connect(self.button7_clicked)# connecting button to a method
        
        self.button8 = QToolButton()
        self.button8.setFixedSize(100, 100) #Enlarging the button
        self.button8.setIconSize(self.button8.size())# Setting the picture in the button
        self.Buttons.append(self.button8)# appending the button to the list
        self.button8.clicked.connect(self.button8_clicked)# connecting button to a method
        
        self.button9 = QToolButton()
        self.button9.setFixedSize(100, 100) #Enlarging the button
        self.button9.setIconSize(self.button9.size())# Setting the picture in the button
        self.Buttons.append(self.button9)# appending the button to the list
        self.button9.clicked.connect(self.button9_clicked)# connecting button to a method
        
        #Create layout
        grid = QGridLayout()
        grid.addWidget(self.welcome,0,0,1,9)
        grid.addWidget(label,1,0)
        grid.addWidget(self.label_edit,1,1,1,1)
        grid.addWidget(self.connect_button,2,1)
        grid.addWidget(messages_label,3,0,1,3)
        grid.addWidget(self.messages_edit,3,0,4,5)
        grid.addWidget(self.button1,5,6)
        grid.addWidget(self.button2,5,7)
        grid.addWidget(self.button3,5,8)
        grid.addWidget(self.button4,6,6)
        grid.addWidget(self.button5,6,7)
        grid.addWidget(self.button6,6,8)
        grid.addWidget(self.button7,7,6)
        grid.addWidget(self.button8,7,7)
        grid.addWidget(self.button9,7,8)
        grid.addWidget(self.Quit_button,8,0)
        grid.addWidget(Game_label,4,6,1,10)
        grid.addWidget(self.pic_label,2,7,2,3)
        grid.addWidget(Shape_label,1,7,1,3)
        grid.addWidget(self.pic_image,0,8,1,4)
        grid.addWidget(self.pic_lab,0,7,1,7)
        grid.addWidget(self.pic_sthombe,0,6,1,1)
        grid.addWidget(self.instruction_button,7,0,2,1)
        self.setLayout(grid) 
        
        # calling a loopthread
        self.otc = LoopThread()
        
        # Connecting the buttons
        self.Quit_button.clicked.connect(self.Quit)
        self.connect_button.clicked.connect(self.connect) 
        self.otc.update_signal.connect(self.handle_message)
        
        # disable all buttons
        for self.button in self.Buttons:
            self.button.setEnabled(False)
    
    # Quit method     
    def Quit(self):
        self.close()
    
    # Connect to the server method
    def connect(self):
        self.server = self.label_edit.text()
        try:
            self.otc.connect_to_server(self.server)
            self.otc.start()
            self.messages_edit.append("Connect to the server")
            self.connect_button.setEnabled(False)
        except:
            self.messages_edit.append('Error connecting to server!,PLEASE ENTER A VALID SERVER NAME!!!')
            
            self.label_edit.clear()
    
    # button method        
    def button1_clicked(self):
        self.otc.moves('0')
    
    # button method 
    def button2_clicked(self):
        self.otc.moves('1')    
    
    # button method 
    def button3_clicked(self):
        self.otc.moves('2')
    
    # button method 
    def button4_clicked(self):
        self.otc.moves('3')
    
    # button method 
    def button5_clicked(self):
        self.otc.moves('4')
    
    # button method     
    def button6_clicked(self):
        self.otc.moves('5')
    
    # button method     
    def button7_clicked(self):
        self.otc.moves('6')
    
    # button method     
    def button8_clicked(self):
        self.otc.moves('7')
    
    # button method     
    def button9_clicked(self):
        self.otc.moves('8')
 
    # message dealing with handling all the methods 
    def handle_message(self, msg_received):
        msg_rec= msg_received.split(",") # splitting the messages received
        if msg_rec[0] == "new game":
            self.messages_edit.append("A new game has begun")
            # Conditions for styling the GUI based on your shape
            if  msg_rec[1] == "X":
                self.pixmap = QPixmap('cross')
                self.pic_label.setPixmap(self.pixmap.scaled(150, 150))
                self.setPalette(QPalette(QColor('red')))                 
            elif msg_rec[1] == "O":
                self.pixmap = QPixmap('nought')
                self.pic_label.setPixmap(self.pixmap.scaled(150, 150))
                self.setPalette(QPalette(QColor('blue'))) 
                
        # Conditions for your move message
        elif msg_rec[0] == "your move":
            self.messages_edit.append(f"it's {msg_received}")
            #Enables all buttons if its not your move
            for button in self.Buttons:
                button.setEnabled(True)
                
        # Conditions for your opponents move    
        elif msg_rec[0] =="opponents move":
            self.messages_edit.append(f"It's {msg_received}....")
            #disables all buttons if its not your move message
            for button in self.Buttons:
                button.setEnabled(False)
                
        # Condition for invalid move message
        elif msg_rec[0]=="invalid move":
            self.messages_edit.append(msg_received)
            
        # Condition for valid move message
        elif msg_rec[0]=="valid move":
            self.messages_edit.append(msg_received)
            # Conditions for inserrting shape on the buttons based on your shape 
            if msg_rec[1] =="X":
                self.Buttons[int(msg_rec[2])].setIcon(QIcon('cross.gif'))
            elif msg_rec[1] =="O":
                self.Buttons[int(msg_rec[2])].setIcon(QIcon('nought.gif'))
                
        # Condition for gameover message
        elif msg_rec[0] == "game over":
            # Conditions for a perfomance on the game
            if msg_rec[1] == "T":
                self.messages_edit.append(f"{msg_rec[0]}..It's a Tie")
            else:
                self.messages_edit.append(f"{msg_rec[0]}..Player {msg_rec[1]} wins the game!!")
        
        # Condition for handling the play again message        
        elif msg_rec[0] == "play again":
            self.play_again = QDialog() # Creating a dialog box
            self.play_again.setWindowTitle('Game over...')
            self.play_again.setGeometry(200,200,300,200)
            self.play_again.setPalette(QPalette(QColor('magenta')))# colouring the dialog box
            self.play = QLabel(f'DO YOU WANT TO PLAY AGAIN?')
            self.play.setFont(QFont('Times',16,3)) #Enlarging the button
            self.yes = QPushButton('YES')
            self.yes.setFont(QFont('Times',16,3))#Enlarging the button
            self.no = QPushButton('NO')
            self.no.setFont(QFont('Times',16,3))#Enlarging the button
            # laying out on the dialog box
            grid = QGridLayout()
            grid.addWidget(self.yes,1,0)
            grid.addWidget(self.no,1,1)
            grid.addWidget(self.play,0,0)
            self.play_again.setLayout(grid)
            # connecting buttons to methods
            self.yes.clicked.connect(self.click_yes)
            self.no.clicked.connect(self.click_no)
            self.play_again.exec_() # execute the dialog box
        
        # Condition for exit game message       
        elif msg_rec[0] == "exit game":
            self.messages_edit.append(msg_received)
    
    # method for allowing to playing again
    def click_yes(self):
        self.otc.moves("y")
        self.clear_board()
        self.play_again.close() # closing the the dialog box if done using the method
        self.messages_edit.append("Starting new game....")
    
    # method for not playing gain    
    def click_no(self):
        self.otc.moves("n")
        self.play_again.close()# closing the the dialog box if done using the method
    
    # method for clearing the game board if you want to play again    
    def clear_board(self):
        for i in range(0,9):
            self.Buttons[int(i)].setIcon(QIcon('blank.gif'))# clearing the board by inserting a blank image to the buttons        
        self.messages_edit.clear()# clearing the message edit
    
    # method for the instructions on how to play the game
    def information(self):
        self.help = QMessageBox() # Creating a message box
        self.help.setWindowTitle('information...')
        self.help.setText("""1. Objective:\n The goal is to form a row of three of your own marks (either “O” or “X”) horizontally, vertically, or diagonally.\n\n2. Setup:\nYou are “O,” and your opponent (either another player or the computer) is “X.”\nThe board consists of 3x3 squares, initially empty.\n\n3. Gameplay:\nPlayers take turns placing their mark in an empty square.\nClick on the button in the grid to place your “O.”\n\n4. Click on the “Play” button in the grid to place your “O.”\n\n5. Strategy:\nAim to create winning line while blocking your opponent from doing the same.\nPay attention to patterns and anticipate your opponent’s moves.\now you’re ready to play! Have fun strategizing and see if you can outwit your opponent!""") # the message passed on the message box            
        self.help.exec_()# executing the message box
        
# main function        
def main():
    app=QApplication(sys.argv)
    Guess = OXOGame()
    Guess.show()
    sys.exit(app.exec_())
main()
