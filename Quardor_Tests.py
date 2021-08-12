# Author: Cameron Bowers
# Date: 08/08/2021
# Description:
# Author: Cameron Bowers
# Date: 7/26/2021
# Description: Test for Linked list

import Quoridor
import unittest

game = Quoridor.QuoridorGame()


class TestingQuoidor(unittest.TestCase):
    """Some tests"""

    def test_1_move_vertical(self):
        """Test adding nodes to a list"""
        print("test_1_move_vertical")
        game.move_pawn(1, (4, 1))
        game.move_pawn(2, (4, 7))
        game.move_pawn(1, (4, 2))
        game.move_pawn(2, (4, 6))
        game.move_pawn(1, (4, 3))
        game.move_pawn(2, (4, 5))
        game.move_pawn(1, (4, 4))
        game.print_board()
        self.assertEqual(game.get_player_board()[4][5], 2)
        self.assertEqual(game.get_player_position(2), (4, 5))
        self.assertEqual(game.get_player_board()[4][4], 1)
        self.assertEqual(game.get_player_position(1), (4, 4))

    def test_2_move_vertical_blocked_by_pawn(self):
        """test the case of a pawn blocking the path"""
        print("test_2_move_vertical_blocked_by_pawn")
        game.move_pawn(2, (4, 4))
        game.print_board()
        # players should not have moved
        self.assertEqual(game.get_player_board()[4][5], 2)
        self.assertEqual(game.get_player_position(2), (4, 5))
        self.assertEqual(game.get_player_board()[4][4], 1)
        self.assertEqual(game.get_player_position(1), (4, 4))
        # is it still player 2's turn
        self.assertEqual(game.get_turn(), 2)

    def test_3_jump(self):
        """Test vertical jumping for player 2"""
        print("test_3_jump")
        game.move_pawn(2, (4, 3))
        game.print_board()
        self.assertEqual(game.get_player_board()[4][3], 2)
        self.assertEqual(game.get_player_position(2), (4, 3))
        self.assertEqual(game.get_player_board()[4][4], 1)
        self.assertEqual(game.get_player_position(1), (4, 4))

    def test_4_place_horizontal_fence(self):
        """Player 1 will place a fence. Note wall board coordinates have an offset"""
        print("test_4_jump_backwards")
        game.place_fence(1, "h", (1, 1))
        self.assertEqual(game.get_horizontal_wall_board()[1][0], "__")

    def test_5_jump_backwards(self):
        """Player 2 jumps backwards"""
        game.move_pawn(2, (4, 5))
        game.print_board()
        self.assertEqual(game.get_player_board()[4][5], 2)
        self.assertEqual(game.get_player_position(2), (4, 5))
        self.assertEqual(game.get_player_board()[4][4], 1)
        self.assertEqual(game.get_player_position(1), (4, 4))

    def test_6_diagonal(self):
        """Test diagonal stuff"""

        # Test illegal diagonal
        game.move_pawn(1, (5, 5))
        game.print_board()
        self.assertEqual(game.get_player_board()[4][5], 2)
        self.assertEqual(game.get_player_position(2), (4, 5))
        self.assertEqual(game.get_player_board()[4][4], 1)
        self.assertEqual(game.get_player_position(1), (4, 4))
        self.assertEqual(game.get_turn(), 1)

        #test legal diagonal right up
        game.place_fence(1, "h", (4, 4))

        game.move_pawn(2, (5, 4))
        game.print_board()
        self.assertEqual(game.get_player_board()[5][4], 2)
        self.assertEqual(game.get_player_position(2), (5, 4))
        self.assertEqual(game.get_player_board()[4][4], 1)
        self.assertEqual(game.get_player_position(1), (4, 4))
        self.assertEqual(game.get_turn(), 1)

if __name__ == '__main__':
    unittest.main()
