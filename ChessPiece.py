#!usr/bin/python

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
        

class Pawn(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "pawn"
        self.moves = []
        
class Queen(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "queen"
        self.moves = ["up", "down", "left", "right", "r_diag", "l_diag"]

class King(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "king"
        self.moves = ["up", "down", "left", "right", "r_diag", "l_diag"]
        
class Rook(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "rook"
        self.moves = []

class Knight(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "knight"
        self.moves = []
            
class Bishop(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "bishop"
        self.moves = []
        
    
if __name__ == '__main__':
    my_piece = ChessPiece("black")
    print my_piece.get_colour()
    
    pawn = Pawn("white")
    print pawn.get_colour()
    print pawn.get_type()
    