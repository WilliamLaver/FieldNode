#!usr/bin/python
from ChessBoard import ChessBoard
from ChessPiece import *
import os
import re

class Chess(object):
    
    def __init__(self):
        self.purpose = "I am a chess game object."
        self.player = [1,'white']
        self.char_map = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
        self.game_over = False
        os.system('cls')
        print "Welcome to Interactive Chess!"
        print "Start Game [yes/y]"
        print "Quit Program [quit/q]"
        response_flag = False
        while(response_flag == False):
            response = raw_input().lower()
            if(response == "yes" or response == "y"):
                response_flag = True
                self.Play_Game()
            elif(response == "quit" or response == "q"):
                response_flag = True
                self.Exit_Program()
            else:
                print "Invalid Response, input [yes/y/quit/q]."
        
    def Play_Game(self):
        play_flag = True
        self.board =  ChessBoard()
        self.display_msg = ""
        
        #game-play loop
        while(play_flag):
            os.system('cls')                    #clear the screen
            print self.display_msg
            if self.display_msg != "":          #display any potential error message
                self.display_msg = ""
            self.board.Populate_Board()         
            self.board.Draw_Board()
            
            #if game won, end the game
            if self.game_over:
                self.Switch_Player()
                print "Player %d Wins!!!"%(self.player[0])
                break
            
            response = raw_input("\nPlayer "+ str(self.player[0]) + " --> ")
            if response == 'quit':
                play_flag = False
                continue
            elif response == "":
                self.display_msg = "ERROR: enter move is 'c2>c4' format only."
                continue
            else:   
                pos = response.split('>')
                
                if len(pos) != 2:
                    self.display_msg = "ERROR: enter move in 'c2>c4' format only."
                    continue
                
                pos = [item[0].upper() + item[1:] for item in pos]
                
                #check formatting of user input, should be c2>c4
                if re.match("^[A-H||a-h][1-8]$",pos[0]) == None or re.match("^[A-H||a-h][1-8]$",pos[1]) == None:
                    self.display_msg = "ERROR: " + pos[0] + ", " + pos[1] + " not valid locations."
                    continue
                
                piece = self.board.board_mapping[pos[0]]
                
                #proceed if chess piece at chosen location
                if isinstance(piece,ChessPiece):
                    
                    #proceed if not moving other player's piece
                    if piece.get_colour() == self.player[1]:
                        
                        #check the status of the move destination
                        destination_clear = self.Check_Destination(piece, pos[1])
                        if not destination_clear:
                            self.display_msg = "ERROR: " + pos[1] + " already occupied."
                            continue
                        
                        #check if the path is clear
                        path_clear = self.Check_Path(piece, pos[1])
                        if not path_clear:
                            self.display_msg = "ERROR: Path from " + pos[0] + " to " + pos[1] + " not clear."
                            continue
                        
                        #attempt to move the piece based on it's legal moves
                        success = piece.move(pos[1])
                        if success == 0:
                            self.display_msg = "ERROR: A " + piece.get_type() + " cannot perform this move."
                            continue
                    else:
                        self.display_msg = "ERROR: Cannot move other player's piece!"
                        continue
                else:
                    self.display_msg = "ERROR: No game-piece at " + pos[0]
                    continue
                
            
            self.Switch_Player()
            
        self.End_Game()
    
    #Switch to the next player's turn
    def Switch_Player(self):
        if self.player[0] == 1:
            self.player = [2, 'black']
        else:
            self.player = [1, 'white']
    
    #check the move destination, if move allowed returns True, otherwise False
    #if opponent's king in destination game ends
    def Check_Destination(self, piece1, destination):
        piece2 = self.board.board_mapping[destination]
        if isinstance(piece2, ChessPiece):
            if piece2.get_colour() == self.player[1]:
                return False
            else:
                if piece2.get_type() == 'king':
                    self.game_over = True
                    self.display_msg = "Game Over!"
                piece2.location = None
                if piece2.get_colour() == 'white':
                    self.board.captured_pieces[0].append(piece2)
                else:
                    self.board.captured_pieces[1].append(piece2)
                return True
        else:
            return True
            
    def Check_Path(self, piece, destination):
        path_clear = True
        if piece.get_type() != 'knight':
            pos = [char for char in piece.location]
            if pos[1] == destination[1]:
                start = self.char_map[pos[0]]
                end = self.char_map[destination[0]]
                if start < end:
                    path = range(start + 1, end)
                else:
                    path = range(end + 1, start)
                    path.reverse()
                path = [string.ascii_uppercase[char - 1] + pos[1] for char in path]
                for loc in path:
                    if isinstance(self.board.board_mapping[loc],ChessPiece):
                        path_clear = False
                        
            elif pos[0] == destination[0]:
                start = int(pos[1])
                end = int(destination[1])
                if start < end:
                    path = range(start + 1, end)
                else:
                    path = range(end + 1, start)
                    path.reverse()
                print path
                path = [pos[0] + str(num) for num in path]
                print path
                for loc in path:
                    if isinstance(self.board.board_mapping[loc],ChessPiece):
                        path_clear = False
                        
            elif abs(self.char_map[destination[0]] - self.char_map[pos[0]]) == abs(int(destination[1]) - int(pos[1])):
                num_start = int(pos[1])
                num_end = int(destination[1])
                char_start = self.char_map[pos[0]]
                char_end = self.char_map[destination[0]]
                
                if num_start < num_end:
                    num_path = range(num_start + 1, num_end)
                else:
                    num_path = range(num_end + 1, num_start)
                    num_path.reverse()
                
                if char_start < char_end:
                    char_path = range(char_start + 1, char_end)
                else:
                    char_path = range(char_end + 1, char_start)
                    char_path.reverse()
                    
                for i in range(len(num_path)):
                    path = [string.ascii_uppercase[char_path[i] - 1] + str(num_path[i]) for i in range(len(num_path))]
                
                for loc in path:
                    if isinstance(self.board.board_mapping[loc],ChessPiece):
                        path_clear = False
                        
        return path_clear
                
    #prompt user to play again, otherwise end program
    def End_Game(self):
        response = raw_input('Press Any Key To Continue')
        myChess = Chess()            
        
    def Exit_Program(self):
        print "Exiting the program"
    
        
#------------------------------------------------------------------------------


if __name__ == '__main__':
    myChess = Chess()
    
    