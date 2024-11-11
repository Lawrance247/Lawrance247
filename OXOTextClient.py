from GameClient import *

class OXOTextClient(GameClient):

    def __init__(self):
        GameClient.__init__(self)
        self.board = [' '] * BOARD_SIZE
        self.shape = None
        
    def clear_board(self):
        self.board = [' '] * BOARD_SIZE
        
    def input_server(self):
        return input('enter server:')
    
    def input_move(self):
        return input('enter move(0-8):')
     
    def input_play_again(self):
        return input('play again(y/n):')

    def display_board(self):
        for i in range(3):
            print(' ' + self.board[i * 3] + ' | ' + self.board[i * 3 + 1] + ' | ' + self.board[i * 3 + 2] + ' ')
            if i < 2:
                print('---|---|---')
   
    def handle_message(self, msg):
        msg1 = msg.split(",")
        if msg1[0] == "new game":
            print("The game has begun...You are",msg1[1])
            self.display_board()
        elif msg1[0] == "your move":
            move = self.input_move()
            self.send_message(move)
        elif msg1[0]=="invalid move":
            print("Invalid move")
        elif msg1[0]=="valid move":
            print("valid move")
            self.P = msg1[2]
            self.shape = msg1[1]
            self.board[int(self.P)] = self.shape
            self.display_board()
             
        elif msg=="opponents move":
            print("It's your Opponents move....")
        elif msg1[0] == "game over":
            if msg1[1] == "T":
                print("It's a Tie")
            else:
                print("Player",msg1[1],"wins the game!!")
        elif msg1[0] == "play again":
            play = self.input_play_again()
            if play == "y":
                self.send_message(play)
                print("Starting new game....")
                self.clear_board()
            elif play=="n":
                self.send_message(play)
                print("Game over!!")
                
        elif msg1[0] == "exit game":
            print("Your partner has exited the game!!")
            
    def play_loop(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.handle_message(msg)
            else: break
            
def main():
    otc = OXOTextClient()
    while True:
        try:
            otc.connect_to_server(otc.input_server())
            break
        except:
            print('Error connecting to server!')
    otc.play_loop()
    input('Press click to exit.')
        
main()


