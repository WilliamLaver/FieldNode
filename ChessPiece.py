#!usr/bin/python

class ChessPiece(object):
    
    def __init__(self, colour):
        self.colour = colour
        self.type = None
    
    def get_colour(self):
        return self.colour
        
    def get_type(self):
        return self.type
        

class Pawn(ChessPiece):
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "pawn"
        
class Queen(ChessPiece):
    def __init(self, colour):
        self.colour = colour
        self.type = "queen"
        self.moves = ["up", "down", "left", "right", ]
        
    
        

if __name__ == '__main__':
    my_piece = ChessPiece("black")
    print my_piece.get_colour()
    
    pawn = Pawn("white")
    print pawn.get_colour()
    print pawn.get_type()
    