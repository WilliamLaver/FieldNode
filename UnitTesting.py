#!usr/bin/python
import unittest
from ChessPiece import *

class TestChessPieces(unittest.TestCase):
        
    def pieces_initialized(self):
        pieces = ["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"]
        for piece in pieces:
            exec("my_piece = " + piece + "('black')")
            self.assertEqual(my_piece.get_type(), piece.lower())
            self.assertEqual(my_piece.get_colour(), "black")
            self.assertIsInstance(my_piece.get_moves(), type([]))
            print
            
        
        print "Pieces initialized correctly if tests pass"        
        
if __name__ == '__main__':
    unittest.main()
    