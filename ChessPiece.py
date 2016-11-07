#!usr/bin/python
import string

class ChessPiece(object):
    def __init__(self, colour):
        self.colour = colour
        self.type = None
        self.location = None
    
    def get_colour(self):
        return self.colour
        
    def get_type(self):
        return self.type
        
    def get_moves(self):
        return self.moves
    
    def __str__(self):
        return self.colour + " " + self.type + " at " + str(self.location)

class Pawn(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "pawn"
        self.moves = []
        if colour == 'white':
            self.symbol = u'\u2659'
            Pawn.numWhite += 1
            self.location = string.ascii_uppercase[Pawn.numWhite - 1] + str(2)
        else:
            self.symbol = u'\u265F'
            Pawn.numBlack += 1
            self.location = string.ascii_uppercase[Pawn.numWhite - 1] + str(7)
        
    
    def get_numWhite(self):
        return Pawn.numWhite
        
    def get_numBlack(self):
        return Pawn.numBlack
        
class Queen(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "queen"
        self.moves = ["up", "down", "left", "right", "r_diag", "l_diag"]
        if colour == 'white':
            self.symbol = u'\u2655'
            Queen.numWhite += 1
            self.location = 'E' + str(1)
        else:
            self.symbol = u'\u265B'
            Queen.numBlack += 1
            self.location = 'E' + str(8)
        
    def get_numWhite(self):
        return Queen.numWhite
    
    def get_numBlack(self):
        return Queen.numBlack

class King(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "king"
        self.moves = ["up", "down", "left", "right", "r_diag", "l_diag"]
        if colour == 'white':
            self.symbol = u'\u2654'
            King.numWhite += 1
            self.location = 'D' + str(1)
        else:
            self.symbol = u'\u265A'
            King.numBlack += 1
            self.location = 'D' + str(8)
        
    def get_numWhite(self):
        return King.numWhite
    
    def get_numBlack(self):
        return King.numBlack
        
class Rook(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "rook"
        self.moves = []
        if colour == 'white':
            self.symbol = u'\u2656'
            Rook.numWhite += 1
            if Rook.numWhite == 1:
                self.location = 'A' + str(1)
            else:
                self.location = 'H' + str(1)
        else:
            self.symbol = u'\u265C'
            Rook.numBlack += 1
            if Rook.numBlack == 1:
                self.location = 'A' + str(8)
            else:
                self.location = 'H' + str(8)
        
    def get_numWhite(self):
        return Rook.numWhite
        
    def get_numBlack(self):
        return Rook.numBlack

class Knight(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "knight"
        self.moves = []
        if colour == 'white':
            self.symbol = u'\u2658'
            Knight.numWhite += 1
            if Knight.numWhite == 1:
                self.location = 'B' + str(1)
            else:
                self.location = 'G' + str(1)
        else:
            self.symbol = u'\u265E'
            Knight.numBlack += 1
            if Knight.numBlack == 1:
                self.location = 'B' + str(8)
            else:
                self.location = 'G' + str(8)
    
    def get_numWhite(self):
        return Knight.numWhite
        
    def get_numBlack(self):
        return Knight.numBlack
            
class Bishop(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "bishop"
        self.moves = []
        if colour == 'white':
            self.symbol = u'\u2657'
            Bishop.numWhite += 1
            if Bishop.numWhite == 1:
                self.location = 'C' + str(1)
            else:
                self.location = 'F' + str(1)
        else:
            self.symbol = u'\u265D'
            Bishop.numBlack += 1
            if Bishop.numBlack == 1:
                self.location = 'C' + str(8)
            else:
                self.location = 'F' + str(8)
    
    def get_numWhite(self):
        return Bishop.numWhite
        
    def get_numBlack(self):
        return Bishop.numBlack
        
    
if __name__ == '__main__':
    my_piece = ChessPiece("black")
   
    