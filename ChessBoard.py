#!usr/bin/python
import string
import sys
from ChessPiece import *

class ChessBoard(object):
    
    def __init__(self):
        pieces = {"King":1, "Queen":1, "Rook":2, "Bishop":2, "Knight":2, "Pawn":8}
        
        #board's pieces attribute should be a list of all pieces
        self.pieces = [[] for i in range(2)]
        self.captured_pieces = [[] for i in range(2)]   #1st array is white pieces, 2nd is black
        self.board_mapping = {}
        self.Initialize_Pieces(pieces)
        self.Populate_Board()
    
    def Initialize_Pieces(self, pieces):
        for key,val in pieces.iteritems():
            exec(str(key) + ".numWhite = 0")
            exec(str(key) + ".numBlack = 0")
            for i in range(val):
                exec("white_piece = " + str(key) + "('white')")
                exec("black_piece = " + str(key) + "('black')")
                self.pieces[0].append(white_piece)
                self.pieces[1].append(black_piece)
                
    
    def Populate_Board(self):
        self.board_mapping = {}
        for i in range(8):
            for j in range(8):
                location = string.ascii_uppercase[j]+str(i+1)
                piece = self.Find_Piece_At_Location(location)
                if piece == None:
                    if (i + j) % 2 == 0:
                        self.board_mapping[location] = u'\u25A1 '#'\u20E3'
                    else:
                        self.board_mapping[location] = u'\u25A0 '
                else:
                    self.board_mapping[location] = piece
        
        
    def Draw_Board(self):
        for i in range(9):
            for j in range(9):
                if i == 0 and j == 0:
                    if sys.platform == 'win32' or sys.platform == 'win64':
                        sys.stdout.write('     ')
                    else:
                        sys.stdout.write('   ')
                elif j == 0:
                    if sys.platform == 'win32' or sys.platform == 'win64':
                        sys.stdout.write(string.ascii_uppercase[8-i]+"   ")
                    else:
                        sys.stdout.write(string.ascii_uppercase[8-i]+"  ")
                elif i == 0:
                    if sys.platform == 'win32' or sys.platform == 'win64':
                        sys.stdout.write(str(j)+ "   ")
                        if j == 4 or j == 6:
                            sys.stdout.write(" ")
                    else:
                        sys.stdout.write(str(j)+ "  ")
                        
                    
                else:
                    location = string.ascii_uppercase[8-i]+str(j)
                    piece = self.board_mapping[location]
                    if isinstance(piece, ChessPiece):
                        sys.stdout.write(piece.symbol + '  ')
                    else:
                        if sys.platform == 'win32' or sys.platform == 'win64':
                            sys.stdout.write(piece + '  ')
                        else:
                            sys.stdout.write(piece + ' ')
            sys.stdout.write('\n')
            sys.stdout.write('\n')
            
        sys.stdout.write('\n')
        for item in self.captured_pieces[0]:
            sys.stdout.write(item.symbol) 
        sys.stdout.write('\n')
        for item in self.captured_pieces[1]:
            sys.stdout.write(item.symbol) 
        sys.stdout.write('\n')
            
                
            
    def Find_Piece_At_Location(self, location):
        chess_piece = None
        for piece in self.pieces[0]:
            if piece.location == location:
                chess_piece = piece
        for piece in self.pieces[1]:
            if piece.location == location:
                chess_piece = piece
        
        return chess_piece
        
if __name__ == '__main__':
    board = ChessBoard()
    for piece in board.pieces[0]:
        print piece
    for piece in board.pieces[1]:
        print piece
    board.Populate_Board()
    board.Draw_Board()
