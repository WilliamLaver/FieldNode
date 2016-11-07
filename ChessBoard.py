#!usr/bin/python
import string
from ChessPiece import *

class ChessBoard(object):
    
    def __init__(self):
        pieces = {"King":1, "Queen":1, "Rook":2, "Bishop":2, "Knight":2, "Pawn":8}
        
        #board's pieces attribute should be a list of all pieces
        self.pieces = []
        self.Initialize_Pieces(pieces)
        self.Populate_Board()
    
    def Initialize_Pieces(self, pieces):
        for key,val in pieces.iteritems():
            for i in range(val):
                exec("white_piece = " + str(key) + "('white')")
                exec("black_piece = " + str(key) + "('black')")
                self.pieces.append(white_piece)
                self.pieces.append(black_piece)
                
            
    def Populate_Board(self):
        self.board = []
        letters = [letter for letter in string.ascii_uppercase][0:8]
        for i in range(8):
            mapping = {}
            for j in range(8):
                print letters[j]+str(i+1)
                mapping[letters[j]+str(i+1)] = 'o'
                
            self.board.append(mapping)
        
        print self.board
        
    def Draw_Board(self):
        
if __name__ == '__main__':
    board = ChessBoard()