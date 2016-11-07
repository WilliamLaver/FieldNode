#!usr/bin/python

class Chess(object):
    
    def __init__(self):
        self.purpose = "I am a chess game object."
        print "------------Welcome to Interactive Chess!--------------"
        print "Start Game [yes/y]"
        print "Quit Program [no/n]"
        response_flag = False
        while(response_flag == False):
            response = raw_input().lower()
            if(response == "yes" or response == "y"):
                response_flag = True
                self.Play_Game()
            elif(response == "no" or response == "n"):
                response_flag = True
                self.Exit_Program()
            else:
                print "Invalid Response, input [yes/y/no/n]."
        
    def Play_Game(self):
        print "Playing The Game"
        
        
    def Exit_Program(self):
        print "Exiting the program"
    
        



if __name__ == '__main__':
    myChess = Chess()
    
    