#!usr/bin/python
from ChessBoard import ChessBoard
from ChessPiece import *
import os
import sys
import re
import random

class Chess(object):
    
    def __init__(self):
        self.purpose = "I am a chess game object."
        self.player = [1,'white']
        self.char_map = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8}
        self.game_over = False
        self.computer_on = False
        
        #clear the screen
        if sys.platform == 'win32' or sys.platform == 'win64':
            os.system('cls')  
        else:
            os.system('clear')
            
        print "Welcome to Interactive Chess!"
        print "Start Game [yes/y]"
        print "Play Computer [ai]"
        print "Quit Program [quit/q]"
        
        response_flag = False
        while(response_flag == False):
            response = raw_input().lower()
            if(response == "yes" or response == "y"):
                response_flag = True
                self.Play_Game()
            elif(response == "ai"):
                response_flag = True
                self.computer_on = True
                self.Play_Game()
            elif(response == "quit" or response == "q"):
                response_flag = True
                self.Exit_Program()
            else:
                print "Invalid Response, input [yes/y/quit/q]."
        
    def Play_Game(self):
        play_flag = True
        self.board =  ChessBoard()
        self.display_msg = "To move a piece from E2 to E4 type 'e2>e4'"
        self.ai_msg = ""
        
        #game-play loop
        while(play_flag):
            
            #clear the screen
            if sys.platform == 'win32' or sys.platform == 'win64':
                os.system('cls')  
            else:
                os.system('clear')                  
            
            #print the AI's latest move
            if self.computer_on:                
                print "   ",self.ai_msg
            
            #display any potential error message
            print self.display_msg
            if self.display_msg != "":          
                self.display_msg = ""
            self.board.Populate_Board()         
            self.board.Draw_Board()
            
            #if game won, end the game
            if self.game_over:
                self.Switch_Player()
                print "Player %d Wins!!!"%(self.player[0])
                break
            
            if self.computer_on and self.player[0] == 2:
                rand_piece = self.board.pieces[1][random.randint(0,len(self.board.pieces[1])-1)]
                clear = False
                n = 0
                while not clear:
                    
                    if n >= len(rand_piece.potential_moves):
                        rand_piece = self.board.pieces[1][random.randint(0,len(self.board.pieces[1])-1)]
                        n = 0
                    
                    rand_dest = rand_piece.potential_moves[random.randint(0,len(rand_piece.potential_moves)-1)]
                    rand_destination_clear = self.Check_Destination(rand_piece,rand_dest)
                    rand_path_clear = self.Check_Path(rand_piece, rand_dest)
                    clear = rand_destination_clear and rand_path_clear
                    n += 1   
                                         
                
                #remove the opposing piece
                if isinstance(self.board.board_mapping[rand_dest],ChessPiece):
                    self.Remove_Piece(rand_dest)
                #move the piece
                self.ai_msg = "AI moved " + rand_piece.__str__() + " to " + rand_dest
                rand_piece.move(rand_dest)
                self.Switch_Player()
                continue
                    
            response = raw_input("Player "+ str(self.player[0]) + " --> ")
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
                            self.display_msg = "ERROR: Cannot move piece to " + pos[1]
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
                        
                        #remove the opposing piece
                        if isinstance(self.board.board_mapping[pos[1]],ChessPiece):
                            self.Remove_Piece(pos[1])
                        
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
                
                if piece1.get_type() == 'pawn':
                    if piece1.location[0] == destination[0]:
                        return False
                        
                if piece2.get_type() == 'king':
                    self.game_over = True
                    self.display_msg = "              Game Over!"
                    self.ai_msg = ""
                    
                return True
        else:
            
            if piece1.get_type() == 'pawn':
                loc_num = self.char_map[piece1.location[0]]
                dest_num = self.char_map[destination[0]]               
                
                if abs(dest_num - loc_num) == abs(int(destination[1]) - int(piece1.location[1])):
                    return False
                    
            return True
            
    def Check_Path(self, piece, destination):
        path_clear = True
        
        if piece.get_type() != 'knight':
            
            pos = [char for char in piece.location]
            #if move is in same column
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
            
            #if move is in same row
            elif pos[0] == destination[0]:
                start = int(pos[1])
                end = int(destination[1])
                if start < end:
                    path = range(start + 1, end)
                else:
                    path = range(end + 1, start)
                    path.reverse()
                    
                path = [pos[0] + str(num) for num in path]
                
                for loc in path:
                    if isinstance(self.board.board_mapping[loc],ChessPiece):
                        path_clear = False
            
            #if move is along a diagonal
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
                    
                path = [string.ascii_uppercase[char_path[i] - 1] + str(num_path[i]) for i in range(len(num_path))]
                
                for loc in path:
                    if isinstance(self.board.board_mapping[loc],ChessPiece):
                        path_clear = False
                        
        return path_clear
        
    def Remove_Piece(self, location):
        piece = self.board.board_mapping[location]
        piece.location = None
        if piece.get_colour() == 'white':
            self.board.captured_pieces[0].append(piece)
            self.board.pieces[0] = self.board.pieces[0][0:self.board.pieces[0].index(piece)]+self.board.pieces[0][self.board.pieces[0].index(piece)+1:]
        else:
            self.board.captured_pieces[1].append(piece)
            self.board.pieces[1] = self.board.pieces[1][0:self.board.pieces[1].index(piece)]+self.board.pieces[1][self.board.pieces[1].index(piece)+1:]
        
    #prompt user to play again, otherwise end program
    def End_Game(self):
        response = raw_input('Press Any Key To Continue\n')
        self.__init__()           
        
    def Exit_Program(self):
        print "Exiting the program"
    
        
#------------------------------------------------------------------------------


if __name__ == '__main__':
    myChess = Chess()
    
    