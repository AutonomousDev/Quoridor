import unittest
# from gradescope_utils.autograder_utils.decorators import weight, visibility
from Quoridor import QuoridorGame

class TestQuoridorGame(unittest.TestCase):
        
        def setUp(self):
            pass
        
        
        #@visibility('visible')
        def test_01(self):
            """Test whether we can create a QuoridorGame object"""
            q = QuoridorGame()

        
        #@visibility('visible')
        def test_02(self):
            """Test whether we can move the pawn from their initial positions"""
            q = QuoridorGame()
            player1_move = q.move_pawn(1, (4,1))
            self.assertTrue(player1_move)
            player2_move = q.move_pawn(2, (4,7))
            self.assertTrue(player2_move)


        
        #@visibility('visible')
        def test_03(self):
            """Test that out of turn moves of pawns cannot be made at the start of the game"""
            q = QuoridorGame()
            player2_move = q.move_pawn(2, (4,7))
            self.assertFalse(player2_move)
 
        
        #@visibility('visible')
        def test_04(self):
            """Test that a horizontal fence can be placed at a valid position, by each player"""
            q = QuoridorGame()
            player1_fence_move = q.place_fence(1, 'h', (6,5))
            self.assertTrue(player1_fence_move)
            player2_fence_move = q.place_fence(2, 'h', (5,5))
            self.assertTrue(player2_fence_move)

        
        #@visibility('visible')
        def test_05(self):
            """Test that a vertical fence can be placed at a valid position, by each player"""
            q = QuoridorGame()
            player1_fence_move = q.place_fence(1, 'v', (3,3))
            self.assertTrue(player1_fence_move)
            player2_fence_move = q.place_fence(2, 'v', (3,4))
            self.assertTrue(player2_fence_move)

        
        #@visibility('visible')
        def test_06(self):
            """Test that lack of win is detected correctly"""
            q = QuoridorGame()
            self.assertFalse(q.is_winner(1))
            self.assertFalse(q.is_winner(2))

        
        #@visibility('after_due_date')
        def test_07(self):
            """Test that vertical fences can't be placed on invalid positions"""
            q = QuoridorGame()
            player1_fence_move = q.place_fence(1, 'v', (-1,0))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (0,-1))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (8,-1))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (1,-8))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (1,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (0,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (-1,8))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (8,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (9,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'v', (-1,-1))
            self.assertFalse(player1_fence_move)

        
        #@visibility('after_due_date')
        def test_08(self):
            """Test that horizontal fences can't be placed on invalid positions"""
            q = QuoridorGame()
            player1_fence_move = q.place_fence(1, 'h', (-1,0))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (0,-1))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (8,-1))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (1,-8))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (1,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (0,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (-1,8))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (8,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (9,9))
            self.assertFalse(player1_fence_move)
            player1_fence_move = q.place_fence(1, 'h', (-1,-1))
            self.assertFalse(player1_fence_move)


        
        #@visibility('after_due_date')
        def test_0901(self):
            """Test that horizontal fences can't be placed where there are already fences by player 1"""
            q = QuoridorGame()
            q.place_fence(1, 'h', (1,1))
            player2_overriding_fence_move = q.place_fence(2, 'h', (1,1))
            self.assertFalse(player2_overriding_fence_move)

        
        #@visibility('after_due_date')
        def test_0902(self):
            """Test that vertical fences can't be placed where there are already fences by player 1"""
            q = QuoridorGame()
            q.place_fence(1, 'v', (1,1))
            player2_overriding_fence_move = q.place_fence(2, 'v', (1,1))
            self.assertFalse(player2_overriding_fence_move)

        
        #@visibility('after_due_date')
        def test_0903(self):
            """Test that horizontal fences can't be placed where there are already fences by player 2"""
            q = QuoridorGame()
            q.place_fence(1, 'h', (1,1))
            q.place_fence(2, 'h', (1,2))
            player1_overriding_fence_move = q.place_fence(1, 'h', (1,2))
            self.assertFalse(player1_overriding_fence_move)

        
        #@visibility('after_due_date')
        def test_0904(self):
            """Test that vertical fences can't be placed where there are already fences by player 2"""
            q = QuoridorGame()
            q.place_fence(1, 'v', (1,1))
            q.place_fence(2, 'v', (1,2))
            player1_overriding_fence_move = q.place_fence(1, 'v', (1,2))
            self.assertFalse(player1_overriding_fence_move)

        
        #@visibility('after_due_date')
        def test_0905(self):
            """Test that vertical fences can't be placed out of turn by player2"""
            q = QuoridorGame()
            out_of_turn_move = q.place_fence(2, 'v', (1,2))
            self.assertFalse(out_of_turn_move)

        
        #@visibility('after_due_date')
        def test_0906(self):
            """Test that vertical fences can't be placed out of turn by player1"""
            q = QuoridorGame()
            q.place_fence(1, 'v', (1,2))
            out_of_turn_move = q.place_fence(1, 'v', (1,3))
            self.assertFalse(out_of_turn_move)

        
        #@visibility('after_due_date')
        def test_0907(self):
            """Test that horizontal fences can't be placed out of turn by player2"""
            q = QuoridorGame()
            out_of_turn_move = q.place_fence(2, 'h', (1,2))
            self.assertFalse(out_of_turn_move)

        
        #@visibility('after_due_date')
        def test_0908(self):
            """Test that horizontal fences can't be placed out of turn by player1"""
            q = QuoridorGame()
            q.place_fence(1, 'h', (1,2))
            out_of_turn_move = q.place_fence(1, 'h', (1,3))
            self.assertFalse(out_of_turn_move)

        
        #@visibility('after_due_date')
        def test_1001(self):
            """Test that pawns can jump over other pawn in the right condition -- player2"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.move_pawn(1, (4,4)) #now they are face to face
            valid_jumping_move = q.move_pawn(2, (4,3))
            self.assertTrue(valid_jumping_move)

        
        #@visibility('after_due_date')
        def test_1002(self):
            """Test that pawns can jump over other pawn in the right condition -- player1"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.place_fence(1, 'h', (8,5))
            q.move_pawn(2, (4,4)) #now they are face to face

            valid_jumping_move = q.move_pawn(1, (4,5)) #jump by player1
            self.assertTrue(valid_jumping_move)

        
        #@visibility('after_due_date')
        def test_1003(self):
            """Test that pawns can't jump over other pawn in the wrong condition -- blocked by fence"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (7,1)) #just so that we can finish the turn 
            
            q.place_fence(1, 'h', (4,4)) #this fence will block the jump

            invalid_jumping_move = q.move_pawn(2, (4,3)) #jump by player 2
            self.assertFalse(invalid_jumping_move)

        
        #@visibility('after_due_date')
        def test_1004(self):
            """Test that pawns can't jump over other pawn in the wrong condition -- with a gap between them"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.place_fence(1, 'h', (8,5))
            invalid_jumping_move = q.move_pawn(2, (4,3)) #jump by player2
            self.assertFalse(invalid_jumping_move)

        
        #@visibility('after_due_date')
        def test_1005(self):
            """Test that pawns can't jump over the fence under any condition -- player1"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.place_fence(2, 'h',(4,2)) #blocking fence

            jumping_over_fence_move = q.move_pawn(1, (4,2))
            self.assertFalse(jumping_over_fence_move)              

        
        #@visibility('after_due_date')
        def test_1006(self):
            """Test that pawns can't jump over the fence under any condition -- player2"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))
            
            q.place_fence(1, 'h', (5,6)) #blocking fence for player2
            q.place_fence(2, 'h', (6,6))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.place_fence(1, 'h', (4,6)) #put fence to block player2
            jumping_over_fence_move = q.move_pawn(2, (4,5)) #should be blocked
            self.assertFalse(jumping_over_fence_move)

        
        #@visibility('after_due_date')
        def test_1007(self):
            """Test that pawns aren't blocked from going into cells which have vertical fences -- player 1"""

            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.place_fence(2, 'v',(4,2)) #non-blocking fence for player1
            move_not_to_be_blocked = q.move_pawn(1, (4,2))
            
            self.assertTrue(move_not_to_be_blocked)

        
        #@visibility('after_due_date')
        def test_1008(self):
            """Test that pawns aren't blocked from going into cells which have vertical fences -- player 2"""

            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.place_fence(2, 'v',(4,3)) #non-blocking fence for player1
            
            q.place_fence(1, 'v', (4,7))
            move_not_to_be_blocked = q.move_pawn(2, (4,7)) 
            
            self.assertTrue(move_not_to_be_blocked)

        
        #@visibility('after_due_date')
        def test_1009(self):
            """Test that a horizontal and vertical fence can be placed in the same coordinate -- player1"""
            q = QuoridorGame()
            q.place_fence(1, 'h', (3,3))
            q.place_fence(2, 'v', (5,6)) 
            
            overriding_fence_move = q.place_fence(1, 'v', (3,3))
            self.assertTrue(overriding_fence_move)

        
        #@visibility('after_due_date')
        def test_1010(self):
            """Test that a horizontal and vertical fence can be placed in the same coordinate -- player2"""
            q = QuoridorGame()
            q.place_fence(1, 'h', (3,3))
            q.place_fence(2, 'v', (5,6)) 
            
            q.place_fence(1, 'v', (5,5))
            overriding_fence_move = q.place_fence(2, 'h', (5,6))
            self.assertTrue(overriding_fence_move)

        
        #@visibility('after_due_date')
        def test_1101(self):
            """Test that pawns can move diagonally in the correct condition -- player2 -- left diagonal"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (7,1)) #just so that we can finish the turn 
            
            q.place_fence(1, 'h', (4,4)) #this fence will block the jump
            left_diagonal_move = q.move_pawn(2, (3,4))
            self.assertTrue(left_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1102(self):
            """Test that pawns can move diagonally in the correct condition -- player2 - right diagonal"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (7,1)) #just so that we can finish the turn 
            
            q.place_fence(1, 'h', (4,4)) #this fence will block the jump by player2
            right_diagonal_move = q.move_pawn(2, (5,4))
            self.assertTrue(right_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1103(self):
            """test that pawns can move diagonally in the correct condition -- player1 -- left diagonal"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (4,6)) #this will block the jump by player1
            
            left_diagonal_move = q.move_pawn(1, (3,5))
            self.assertTrue(left_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1104(self):
            """Test that pawns can move diagonally in the correct condition -- player1 - right diagonal"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (4,6)) #this will block the jump by player1
            
            right_diagonal_move = q.move_pawn(1, (5,5))
            self.assertTrue(right_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1105(self):
            """Test that pawns can't move diagonally right in the wrong conditions -- when there is no wall blocking the jump -- player1"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (6,6)) #this will *not* block the jump by player1
            
            wrong_right_diagonal_move = q.move_pawn(1, (5,5))
            self.assertFalse(wrong_right_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1106(self):
            """Test that pawns can't move diagonally left in the wrong conditions -- when there is no wall blocking the jump -- player1"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (6,6)) #this will *not* block the jump by player1
            
            wrong_left_diagonal_move = q.move_pawn(1, (3,5))
            self.assertFalse(wrong_left_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1107(self):
            """Test that pawns can't move diagonally left in the wrong conditions -- when there is no wall blocking the jump -- player2"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (7,1)) #just so that we can finish the turn 
            
            q.place_fence(1, 'h', (6,6)) #this fence will *not* block the jump

            wrong_left_diagonal_move = q.move_pawn(2, (3,4))
            self.assertFalse(wrong_left_diagonal_move)

        
        #@visibility('after_due_date')
        def test_1108(self):
            """Test that pawns can't move diagonally right in the wrong conditions -- when there is no wall blocking the jump -- player2"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))
            
            q.move_pawn(1, (4,4)) #now they are face to face
            q.place_fence(2, 'h', (7,1)) #just so that we can finish the turn 
            
            q.place_fence(1, 'h', (6,6)) #this fence will *not* block the jump by player2

            wrong_right_diagonal_move = q.move_pawn(2, (5,4))
            self.assertFalse(wrong_right_diagonal_move)

        
        #@visibility('after_due_date')
        def test_12(self):
            """Test that an accurate count of fences is kept, by putting all fences and trying to put more"""
            q = QuoridorGame()
            
            for i in range(0,9):
                print(i)
                q.place_fence(1, 'v', (7,i))
                q.place_fence(2, 'v', (2,i))
            
            #put the 10th fence
            print(10)
            q.place_fence(1, 'h', (3,6))
            q.place_fence(2, 'h', (5,6))
 
            #try putting the 11th fence
            print(11)
            illegal_fence_placement_move_1 = q.place_fence(1, 'v', (6,6))
            self.assertFalse(illegal_fence_placement_move_1)

            illegal_fence_placement_move_2 = q.place_fence(2, 'v', (6,5))
            self.assertFalse(illegal_fence_placement_move_2)

        
        #@visibility('after_due_date')
        def test_13(self):
            """Test that a pawn cannot be at two places, by making sure it's position is updated correctly"""
            q = QuoridorGame()
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            illegal_move_player_1 = q.move_pawn(1, (4,1))
            self.assertFalse(illegal_move_player_1)

            illegal_move_player_2 = q.move_pawn(2, (4,7))
            self.assertFalse(illegal_move_player_2)

        
        #@visibility('after_due_date')
        def test_1401(self):
            """Test that after Player2 pawn has reached the baseline, the Player1 cannot make any move"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.move_pawn(1, (4,4))
            q.move_pawn(2, (4,3)) #jumped

            q.move_pawn(1, (4,5))
            q.move_pawn(2, (4,2))

            q.move_pawn(1, (4,6))
            q.move_pawn(2, (4,1))

            q.move_pawn(1, (4,7))
            q.move_pawn(2, (4,0)) #wins

            move_after_win = q.place_fence(1,'h',(2,1))
            self.assertFalse(move_after_win)

        
        #@visibility('after_due_date')
        def test_1402(self):
            """Test that after Player1 pawn has reached the baseline, the Player2 cannot make any move"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.move_pawn(1, (4,4))
            q.move_pawn(2, (4,3)) #jumped

            q.move_pawn(1, (4,5))
            q.move_pawn(2, (4,2))

            q.move_pawn(1, (4,6))
            q.move_pawn(2, (4,1))

            q.move_pawn(1, (4,7))
            q.place_fence(2, 'h', (6,5))

            q.move_pawn(1, (4,8)) #wins

            move_after_win = q.place_fence(2,'h',(2,1))
            self.assertFalse(move_after_win)

        
        #@visibility('after_due_date')
        def test_1403(self):
            """Test that a win is correctly detected -- player2"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.move_pawn(1, (4,4))
            q.move_pawn(2, (4,3)) #jumped

            q.move_pawn(1, (4,5))
            q.move_pawn(2, (4,2))

            q.move_pawn(1, (4,6))
            q.move_pawn(2, (4,1))

            q.move_pawn(1, (4,7))
            q.move_pawn(2, (4,0)) #wins

            self.assertTrue(q.is_winner(2))
            self.assertFalse(q.is_winner(1))

        
        #@visibility('after_due_date')
        def test_1404(self):
            """Test that a win is correctly detected -- player1"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            q.move_pawn(1, (4,3))
            q.move_pawn(2, (4,5))

            q.move_pawn(1, (4,4))
            q.move_pawn(2, (4,3)) #jumped

            q.move_pawn(1, (4,5))
            q.move_pawn(2, (4,2))

            q.move_pawn(1, (4,6))
            q.move_pawn(2, (4,1))

            q.move_pawn(1, (4,7))
            q.place_fence(2, 'h', (6,5))

            q.move_pawn(1, (4,8))

            self.assertTrue(q.is_winner(1))
            self.assertFalse(q.is_winner(2))

        
        #@visibility('after_due_date')
        def test_1405(self):
            """Test that reaching own baseline isn't detected as win -- player1"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            #now start going back
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,0)) #player1 has moved to own baseline
            self.assertFalse(q.is_winner(1))

            move_after_false_win = q.move_pawn(2, (4,6))
            self.assertTrue(move_after_false_win)

        
        #@visibility('after_due_date')
        def test_1406(self):
            """Test that reaching own baseline isn't detected as win -- player2"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.move_pawn(2, (4,6))

            #now start going back
            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.place_fence(1, 'h',(5,6)) #make a move to pass the turn 
            q.move_pawn(2, (4,8)) #player2 has moved to own baseline
            self.assertFalse(q.is_winner(2))

            move_after_false_win = q.move_pawn(1, (4,2))
            self.assertTrue(move_after_false_win)

        
        #@visibility('after_due_date')
        def test_1501(self):
            """EXTRA CREDIT: Test that fair play rule has been implemented -- blocking baseline isn't allowed"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.place_fence(2, 'h', (0,8)) #p2 starts putting fence

            q.move_pawn(1, (4,3))
            q.place_fence(2, 'h', (1,8)) 

            q.move_pawn(1, (4,4))
            q.place_fence(2, 'h', (2,8)) 

            q.move_pawn(1, (4,5))
            q.place_fence(2, 'h', (3,8)) 

            q.move_pawn(1, (4,6))
            q.place_fence(2, 'h', (4,8)) 

            q.move_pawn(1, (5,6)) #move horizontally so P2 gets enough turns to fence
            q.place_fence(2, 'h', (5,8)) 

            q.move_pawn(1, (4,6)) #move horizontally so P2 gets enough turns to fence
            q.place_fence(2, 'h', (6,8)) 

            q.move_pawn(1, (5,6)) #move horizontally so P2 gets enough turns to fence
            q.place_fence(2, 'h', (7,8)) 

            q.move_pawn(1, (4,6)) #move horizontally so P2 gets enough turns to fence
            last_blocking_fence_placement_move = q.place_fence(2, 'h', (8,8)) #last fence block

            self.assertEqual(last_blocking_fence_placement_move, "breaks the fair play rule")

        
        #@visibility('after_due_date')
        def test_1502(self):
            """EXTRA CREDIT: Test that fair play rule has been implemented -- surrounding a pawn with fences on all sides"""
            q = QuoridorGame()

            q.move_pawn(1, (4,1))
            q.move_pawn(2, (4,7))

            q.move_pawn(1, (4,2))
            q.place_fence(2, 'v', (4,2)) #p2 starts putting fence left fence

            q.place_fence(1, 'v', (7,1)) #dumb move to pass
            q.place_fence(2, 'v', (5,2)) #right fence

            q.place_fence(1,'v', (7,3)) #dumb move to pass
            q.place_fence(2, 'h', (4,2)) #northern fence

            q.place_fence(1, 'v', (7,2)) #dumb move to pass
            last_blocking_fence_placement_move = q.place_fence(2, 'h', (4,3)) #southern fence block that would trap p2

            self.assertEqual(last_blocking_fence_placement_move, "breaks the fair play rule")

