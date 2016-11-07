#!usr/bin/python
import string
import sys
from ChessPiece import *

class ChessBoard(object):
    
    def __init__(self):
        pieces = {"King":1, "Queen":1, "Rook":2, "Bishop":2, "Knight":2, "Pawn":8}
        
        #board's pieces attribute should be a list of all pieces
        self.pieces = []
        self.Initialize_Pieces(pieces)
        self.Populate_Board()
        self.Draw_Board()
    
    def Initialize_Pieces(self, pieces):
        for key,val in pieces.iteritems():
            for i in range(val):
                exec("white_piece = " + str(key) + "('white')")
                exec("black_piece = " + str(key) + "('black')")
                self.pieces.append(white_piece)
                self.pieces.append(black_piece)
                
    
    def Populate_Board(self):
        self.board_mapping = {}
        for i in range(8):
            for j in range(8):
                location = string.ascii_uppercase[j]+str(i+1)
                piece = self.Find_Piece_At_Location(location)
                if piece == None:
                    self.board_mapping[location] = '# '
                else:
                    self.board_mapping[location] = piece.symbol
        
        
    def Draw_Board(self):
        for i in range(9):
            for j in range(9):
                if i == 0 and j == 0:
                    sys.stdout.write('  ')
                elif j == 0:
                    sys.stdout.write(string.ascii_uppercase[8-i]+" ")
                elif i == 0:
                    sys.stdout.write(str(j)+ " ")
                else:
                    location = string.ascii_uppercase[8-i]+str(j)
                    sys.stdout.write(self.board_mapping[location])
            sys.stdout.write('\n')
            
    def Find_Piece_At_Location(self, location):
        chess_piece = None
        for piece in self.pieces:
            if piece.location == location:
                chess_piece = piece
        
        return chess_piece
        
if __name__ == '__main__':
    board = ChessBoard()
   