#!usr/bin/python
from ChessBoard import ChessBoard
from ChessPiece import *
import os
import sys
import re

class Chess(object):
    
    def __init__(self):
        self.purpose = "I am a chess game object."
        self.player = [1,'white']
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
                
                if isinstance(piece,ChessPiece):
                    if piece.get_colour() == self.player[1]:
                        destination_clear = self.Check_Destination(piece, pos[1])
                        if not destination_clear:
                            self.display_msg = "ERROR: " + pos[1] + " already occupied."
                            continue
                        piece.move(pos[1])
                    else:
                        self.display_msg = "ERROR: Cannot move other player's piece!"
                        continue
                else:
                    self.display_msg = "ERROR: No game-piece at " + pos[0]
                    continue
                
            
            self.Switch_Player()
            
        self.End_Game()
        
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
                self.display_msg = "Switching with game-piece"
                if piece2.get_type() == 'king':
                    self.game_over = True
                    self.display_msg = "Game Over!"
                piece2.location = None
                return True
        else:
            return True
    
    #prompt user to play again, otherwise end program
    def End_Game(self):
        response = raw_input('Press Any Key To Continue')
        myChess = Chess()            
        
    def Exit_Program(self):
        print "Exiting the program"
    
        
#------------------------------------------------------------------------------


if __name__ == '__main__':
    myChess = Chess()
    
    