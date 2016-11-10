#!usr/bin/python
import string

class ChessPiece(object):
    def __init__(self, colour):
        self.colour = colour
        self.type = None
        self.location = None
        self.has_moved = False
        self.potential_moves = []
    
    def get_colour(self):
        return self.colour
        
    def get_type(self):
        return self.type
        
    def get_moves(self):
        return self.moves
        
    def move(self, destination):
        if destination in self.potential_moves:
            self.has_moved = True
            self.location = destination
            self.Find_Potential_Moves()
            return 1
        else:
            return 0
        
    
    def __str__(self):
        return self.colour + " " + self.type + " at " + str(self.location)
        

class Pawn(ChessPiece):
    numWhite = 0
    numBlack = 0
    def __init__(self, colour):
        ChessPiece.__init__(self, colour)
        self.colour = colour
        self.type = "pawn"
        if colour == 'white':
            self.symbol = u'\u2659'
            Pawn.numWhite += 1
            self.location = string.ascii_uppercase[Pawn.numWhite - 1] + str(2)
        else:
            self.symbol = u'\u265F'
            Pawn.numBlack += 1
            self.location = string.ascii_uppercase[Pawn.numWhite - 1] + str(7)
    
        self.Find_Potential_Moves()
    
    def Find_Potential_Moves(self):
        if self.location == None:
            return None
            
        if self.colour == 'white':
            forward = 1
        else:
            forward = -1
        self.potential_moves = []
        pos = [char for char in self.location]
        if int(pos[1]) == 2 and self.colour == 'white':
            self.potential_moves.append(pos[0] + '4')
        elif int(pos[1]) == 7 and self.colour == 'black':
            self.potential_moves.append(pos[0] + '5')
        letter_pos = [char for char in string.ascii_uppercase].index(pos[0])
        for i in range(8):
            for j in range(1,9):
                if (i == letter_pos + 1 or i == letter_pos - 1 or i == letter_pos) and j == int(pos[1]) + forward:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
    
        
    
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
            
        self.Find_Potential_Moves()
    
    def Find_Potential_Moves(self):
        if self.location == None:
            return None
        self.potential_moves = []
        pos = [char for char in self.location]
        letter_pos = [char for char in string.ascii_uppercase].index(pos[0])
        for i in range(8):
            for j in range(1,9):
                if abs(i - letter_pos) == abs(j - int(pos[1])) or string.ascii_uppercase[i] == pos[0] or j == int(pos[1]):
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
        
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
            
        self.Find_Potential_Moves()
            
    def Find_Potential_Moves(self):
        if self.location == None:
            return None
        self.potential_moves = []
        pos = [char for char in self.location]
        letter_pos = [char for char in string.ascii_uppercase].index(pos[0])
        for i in range(8):
            for j in range(1,9):
                if (i == letter_pos - 1 or i == letter_pos + 1 or i == letter_pos) and (j == int(pos[1]) or j == int(pos[1]) + 1 or j == int(pos[1]) - 1):
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
        
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
        self.potential_moves = []
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
                
        self.Find_Potential_Moves()
    
    def Find_Potential_Moves(self):
        if self.location == None:
            return None
        self.potential_moves = []
        pos = [char for char in self.location]
        for i in range(8):
            for j in range(1,9):
                letter = string.ascii_uppercase[i]
                if letter == pos[0] or j == int(pos[1]):
                    self.potential_moves.append(letter + str(j))
        
        
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
                
        self.Find_Potential_Moves()
            
    def Find_Potential_Moves(self):
        if self.location == None:
            return None
        self.potential_moves = []
        pos = [char for char in self.location]
        letter_pos = [char for char in string.ascii_uppercase].index(pos[0])
        for i in range(8):
            for j in range(1,9):
                if i == letter_pos - 1 and j == int(pos[1]) - 2:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos - 1 and j == int(pos[1]) + 2:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos - 2 and j == int(pos[1]) - 1:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos - 2 and j == int(pos[1]) + 1:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos + 2 and j == int(pos[1]) + 1:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos + 2 and j == int(pos[1]) - 1:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos + 1 and j == int(pos[1]) + 2:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                elif i == letter_pos + 1 and j == int(pos[1]) - 2:
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
                
    
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
                
        self.Find_Potential_Moves()
    
    def Find_Potential_Moves(self):
        if self.location == None:
            return None
        self.potential_moves = []
        pos = [char for char in self.location]
        letter_pos = [char for char in string.ascii_uppercase].index(pos[0])
        for i in range(8):
            for j in range(1,9):
                if abs(i - letter_pos) == abs(j - int(pos[1])):
                    self.potential_moves.append(string.ascii_uppercase[i] + str(j))
    
    def get_numWhite(self):
        return Bishop.numWhite
        
    def get_numBlack(self):
        return Bishop.numBlack
        
    
if __name__ == '__main__':
    my_piece = ChessPiece("black")
    knight = Knight('black')
    knight.move('B8')
    print knight.potential_moves
    print knight.__str__()
    
    
   
    