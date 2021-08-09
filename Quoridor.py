# Author: Cameron Bowers
# Date: 08/03/2021
# Description: This program is a game called quoridor

"""
DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
    Determining how to store the board.
        The board is broken down into 3 parts. a _player_board, _vertical_wall_board and a _horizontal_wall_board. Each
        are a list of list such that board[x][y] uses the first index is the list for x coordinates and the second is
        the index for y coordinates. All 3 boards are stored in __init__

    Initializing the board
        To initialize the board the _generate_board method is used. For each of the _player_board, _vertical_wall_board
        and _horizontal_wall_board, a list of the correct y length is created with a FOR loop. It is then copied for the
        correct number of x positions. Strings for the spaces are filled during generation. The 3 finished boards are
        returned to __init__() and stored.

    Determining how to track which player's turn it is to play right now.
        To track the players turn there is a variable in __init__() called _turn and a get_turn() method. Placing fences
        and moving the player calls this method to check if the move is valid.

    Determining how to validate a moving of the pawn.
        To check if the move is legal with a sub method and return true of false. To do this it will check,
            * Is it this players turn? call get_turn() and compare against he player perimeter
            * Is the game over? return true/false
            * is the space open? return true/false
            * is the space horizontal or vertical? Needed to check the correct fence board.
            * is a fence in between horizontally or vertically? return true/false
            * is the move legal with jumping a pawn rule? return true/false for this special case.

    Determining how to validate placing of the fences.
        To check if a fence placement is legal,
            * Check if it's the players turn using get_turn() and the player parameters.
            * Check the player has fences left using get_fences_remaining() and the player parameters.
            * Offset the coordinates to match the expected space for the Vertical or Horizontal board.
            * Call _fence_coordinate_check() to validate direction and coordinates as in range
            * Call _check_fence_placement() to make sure the space is open. if true:
                * _use_a_fences(player) to reduce the number of fences for player
                * _set_fence_space() to place the fence on the correct board at the coordinates.
                * next_turn() ends the turn.

        Determining how to keep track of fences on the board and off the board.
            To track fences off the board 2 variables called _player1_fences and _player2_fences exist in __init__().
            To track fences on the board 2 co boards exist called _vertical_wall_board and _horizontal_wall_board.
            Fences are marked with __ or | ascii characters for look beautiful when printing the board. When
            the player tries to place a fence or move the correct boards is checked for a open space of clear path.

        Determining how to keep track of the pawn's position on the board.
            To track the players position a co-board exist called _player_board stored in __init__(). pawn positions are
            marked as a 1 or a 2. After each move the new position is updated and the old position is cleared. the board
            uses □ ascii characters to represent spaces and look pretty when printing the board.
"""


class QuoridorGame:
    """The Quoridor class contains everything needed to play the game"""

    def _generate_board(self):
        """This method is called by __init__ to return a generated blank board. The blank board has 3 sub boards. One
        tracks the player positions. One tracks the Horizontal walls. one tracks vertical walls. each board is a list
        containing sub lists such that you can access coordinates with my_list_name[x][y] Empty player positions will
        be tracked with the □ ascii character. empty wall position will be tracked with "  " strings. """
        y_player_row = []
        for i in range(9):
            y_player_row.append("□")
        x_player_row = []
        for i in range(9):
            x_player_row.append(y_player_row.copy())

        vertical_y_wall_row = []
        for i in range(9):
            vertical_y_wall_row.append("  ")

        vertical_x_wall_row = []
        for i in range(8):
            vertical_x_wall_row.append(vertical_y_wall_row.copy())

        horizontal_y_wall_row = []
        for i in range(8):
            horizontal_y_wall_row.append("  ")

        horizontal_x_wall_row = []
        for i in range(9):
            horizontal_x_wall_row.append(horizontal_y_wall_row.copy())

        return x_player_row, vertical_x_wall_row, horizontal_x_wall_row

    def __init__(self):
        """Initialize variables. The __init__ method will:
            * call _generate_board() to create blank boards
            * Store the boards for player, horizontal wall and vertical wall for use through out our program.
            * Set the starting player positions by calling set_player_board_space().
            * Initialize the current turn to player 1 and track it's value as updated.
            * Initialize variable to track how many fences each player have remaining.
         """
        # Generate the boards
        self._player_board, self._vertical_wall_board, self._horizontal_wall_board = self._generate_board()

        # Set player starting positions
        self._player1_position = (4, 0)
        self._player2_position = (4, 8)

        self.set_player_board_space(1, 4, 0)
        self.set_player_board_space(2, 4, 8)

        self._turn = 1  # 1 is player 1, 2 is player 2

        # track number of fence each player has left
        self._player1_fences = 10
        self._player2_fences = 10

        self._game_over = False

    def get_player_board(self):
        """Returns the player board"""
        return self._player_board

    def set_player_board_space(self, value, x, y):
        """sets a space on the player board to value"""
        self._player_board[x][y] = value

    def get_vertical_wall_board(self):
        """Returns the vertical wall board"""
        return self._vertical_wall_board

    def get_horizontal_wall_board(self):
        """Return the Horizontal wall board"""
        return self._horizontal_wall_board

    def fence_space_inspector(self, direction: str, coord: tuple):
        """Inspects a space for fences to handle the offsets. direction 'h' for horizontal fences, 'v' for vertical
        fences returns true if a fence is in the way"""
        if coord[0] < 0 or coord[0] > 8 or coord[1] < 0 or coord[1] > 8:
            return False  # space out of bounds
        # Horizontal wall check
        if direction == "h":
            if coord[1] ==0:
                return False  # y=0 can't have fences
            elif self.get_horizontal_wall_board()[coord[0]][coord[1]-1] == "  ":
                return True
        # Vertical wall check
        if direction == "v":
            if coord[0] == 0:
                return False  # x=0 can't have fences
            elif self.get_horizontal_wall_board()[coord[0]-1][coord[1]] == "  ":
                return True  # Space is open

    def get_turn(self):
        """Return the current turn"""
        return self._turn

    def check_turn(self, player):
        """Returns true of false if it's this players turn"""
        if player == self.get_turn():
            return True
        else:
            print("It is not your turn player", player)
            return False

    def next_turn(self):
        """This method changes the turn to the other players turn. It will be called by placing a wall or moving a
        player """
        if self.get_turn() == 1:
            self._turn = 2
        elif self.get_turn() == 2:
            self._turn = 1

    def get_player_position(self, player):
        """Returns the position of the player piece"""
        if player == 1:
            return self._player1_position
        elif player == 2:
            return self._player2_position
        else:
            print("Invalid player number. int 1 or 2 expected")

    def set_player_position(self, player, coords: tuple):
        """Sets the player position to a new value"""
        if player == 1:
            self._player1_position = coords
        elif player == 2:
            self._player2_position = coords
        else:
            print("invalid player")

    def get_game_over(self):
        """Returns true of false value of _game_over"""
        if self._game_over:
            print("The game is over")
            return self._game_over
        else:
            return self._game_over

    def get_fences_remaining(self, player):
        """returns the number of fences the player parameters has remaining. This method is used as a check in
        place_fence() to make sure the player has enough fences left. """
        if player == 1:
            return self._player1_fences
        elif player == 2:
            return self._player2_fences
        else:
            print("invalid player?")

    def _use_a_fences(self, player):
        """Reduces the fences remaining by 1 for player parameters. This method is used at the conclusion of the
        place_fence()."""
        if player == 1:
            self._player1_fences -= 1
        elif player == 2:
            self._player2_fences -= 1
        else:
            print("invalid player?")

    def _composite_board(self, debug=None):
        """The method is part of the print board process. It composites the player and wall boards in preparation to
        display a beautiful ascii board in the console. This function places ⚫ characters where walls can come
        together for spacing. The master board returned will be a list of lists."""
        master_board = []
        vertical_spacer = "⚫"
        if debug == "debug":
            vertical_spacer = "  ⚫  "

        for x in range(len(self.get_player_board())):
            master_board.append(self.get_player_board()[x].copy())

        for x in range(len(self.get_horizontal_wall_board())):
            for y in range(len(self.get_horizontal_wall_board()[x])):
                master_board[x].insert(2 * y + 1, self.get_horizontal_wall_board()[x][y])

        for x in range(len(self.get_vertical_wall_board())):
            if x < len(self.get_vertical_wall_board()):
                master_board.insert(2 * x + 1, self.get_vertical_wall_board()[x].copy())
                for y in range(len(master_board[2 * x + 1]) - 1):
                    master_board[2 * x + 1].insert(-1 - 2 * y, vertical_spacer)
        return master_board

    def print_board(self, debug=None):
        """Prints the game board to console.
            * This method calls composite_board() to get a list that contains the
        wall and player boards.
            * To do this a list of 17 strings is made. Then it cycles through the master board we
        generated converting each list item in to a single string for the line string. Because our master list is [
        x][y] we can't just print the list of list or the orientation will be wrong in the console with x running
        vertically and y horizontally. We reference each list item by coordinate to get them ordered and oriented
        correctly. """

        print("________Current Board_________")  # This header helps seperate the board from previous print_board()
        # outputs
        if debug == "debug":
            master_board = self._composite_board("debug")
        else:
            master_board = self._composite_board()
        results = []
        for i in range(17):
            results.append("")

        for x in range(len(master_board)):
            for y in range(len(master_board[x])):
                results[y] += str(master_board[x][y])

        for x in range(len(results)):
            print(results[x])

    def _debug_board_coord(self):
        """Replaces every player square and wall board square with it's coordinates then prints. This method is used
        for debugging to verify which positions are which. All player and all data is overwritten. At the end it calls
        print_board() """
        for x in range(len(self.get_player_board())):
            for y in range(len(self.get_player_board()[x])):
                coord = "(" + str(x) + "," + str(y) + ")"
                self.set_player_board_space(coord, x, y)

        for x in range(len(self.get_vertical_wall_board())):
            for y in range(len(self.get_vertical_wall_board()[x])):
                v_coord = "[V" + str(x) + "," + str(y) + "]"
                self._debug_fence_board(v_coord, x, y, "v")

        for x in range(len(self.get_horizontal_wall_board())):
            for y in range(len(self.get_horizontal_wall_board()[x])):
                h_coord = "[H" + str(x) + "," + str(y) + "]"
                self._debug_fence_board(h_coord, x, y, "h")

        self.print_board("debug")

    def _move_space_open(self, coord: tuple):
        """Checks if the space is open for a move"""
        if self.get_player_board()[coord[0]][coord[1]] == "□":
            return True
        else:
            return False  # this space is occupied

    def _move_path_check(self, coord: tuple, player: int):
        """Checks the move path for walls and stuff. returns true or false if the path is legal"""
        move_type = None
        delta_movement = [0, 0]
        player_position = self.get_player_position(player)
        delta_movement[0] = coord[0] - player_position[0]
        delta_movement[1] = coord[1] - player_position[1]

        # Check if movement is vertical?
        if delta_movement == [0, -1] or delta_movement == [0, 1]:
            move_type = "vertical"
            if self._basic_move_check(coord, player, move_type, delta_movement):
                return True  # No walls in the way
            else:
                return False  # There is a wall in the way
        # Is movement horizontal?
        elif delta_movement == [-1, 0] or delta_movement == [1, 0]:
            move_type = "horizontal"
            if self._basic_move_check(coord, player, move_type, delta_movement):
                return True  # No walls in the way
            else:
                return False  # There is a wall in the way
        # Is movement diagonal?
        elif delta_movement == [-1, -1] or delta_movement == [-1, 1] or delta_movement == [1, 1] or delta_movement == [
            1, -1]:
            move_type = "diagonal"
            if self._diagonal_move_check(coord, player, move_type, delta_movement):
                return True
            else:
                return False
        # Is it a Jump
        elif delta_movement == [0, 2] or delta_movement == [0, -2] or delta_movement == [2, 0] or delta_movement == [-2,
                                                                                                                     0]:
            move_type = "jump"
            if self._jump_move_check(coord, player, move_type, delta_movement):
                return True
            else:
                return False
        else:
            return False  # illegal move distance

    def _basic_move_check(self, coord: tuple, player, direction, delta_movement):
        """Used for horizontal and vertical movement. Returns true if move is not blocked by walls"""
        wall_board = None

        if direction == "vertical":
            wall_board = self.get_horizontal_wall_board()
            delta_movement[1] -= 2  # offset coordinates for the wall board
        elif direction == "horizontal":
            wall_board = self.get_vertical_wall_board()
            delta_movement[0] += 1  # offset coordinates for the wall board

        fence_check_position = [coord[0] + delta_movement[0], coord[1] + delta_movement[1]]
        if wall_board[fence_check_position[0]][fence_check_position[1]] == "  ":
            return True
        return False

    def _diagonal_move_check(self, coord: tuple, player, direction, delta_movement):
        """Used for the case of moving diagonally if another pawn blocks the path"""
        vertical_fence_offset = [delta_movement[0], delta_movement[1] - 2]
        vertical_wall_board = self.get_vertical_wall_board()
        vertical_wall_check_coords = coord[0] + vertical_fence_offset[0]
        # ^Incomplete? todo
        horizontal_fence_offset = [delta_movement[0] + 1, delta_movement[1]]
        horizontal_wall_board = self.get_horizontal_wall_board()

        player_position = self.get_player_position(player)
        if not self._move_space_open((player_position[0], player_position[1] + delta_movement[1])):
            # The vertical space in the direction we are moving diagonally in is blocked by a player.
            my_var = [player_position[0], player_position[1] + horizontal_fence_offset[1]]
            my_other_var = horizontal_wall_board[my_var[0]][my_var[1]]
            if not self.fence_space_inspector(h, (player_position[0], player_position[1]+delta_movement[1]*2)):
            if horizontal_wall_board[player_position[0]][(player_position[1] + horizontal_fence_offset[1] - 1)] != "  ":
                # There is a fence behind the other player
                # todo finish this function with additional wall checks depending on instructor reply on ed discussion
                return True
        return False

    def _jump_move_check(self, coord, player, move_type, delta_movement):
        """Used for the case of moving diagonally if another pawn blocks the path"""

        horizontal_fence_offset = [delta_movement[0] + 1, delta_movement[1]]
        horizontal_wall_board = self.get_horizontal_wall_board()

        player_position = self.get_player_position(player)
        if self._move_space_open((player_position[0], player_position[1] + delta_movement[1])):
            # The vertical space in the direction we are moving diagonally in is blocked by a player.
            if horizontal_wall_board[player_position[0]][(player_position[1] + horizontal_fence_offset[1])] == "  ":
                # There is a no fence behind the other player
                return True  # Jump is legal

    def _move_check(self, player: int, coord: tuple):
        """
         check if the move is legal with a sub method and return true of false
            * Is it this players turn? call get_turn() and compare against he player perimeter
            * Is the game over? return true/false
            * is the space open? return true/false
            * is the space horizontal or vertical? Needed to check the correct fence board.
            * is a fence in between horizontally or vertically? return true/false
            * is the move legal with jumping a pawn rule? return true/false for this special case.
        """
        if not self.check_turn(player):
            return False  # It's not this players turn
        if self.get_game_over():
            return False  # The game is over
        # todo Check coordinate is on the game board
        if not self._move_space_open(coord):
            return False  # This space is occupied
        if not self._move_path_check(coord, player):
            return False  # The move is blocked by a wall or illegal distance

        return True  # Passed all checks

    def move_pawn(self, player: int, coord: tuple):
        """This function will move a pawn once it's finished. It will take a player and coordinate parameter. To do this,
        * check if the move is legal with a sub method and return true of false
            * Is it this players turn? call get_turn() and compare against he player perimeter
            * Is the game over? return true/false
            * is the space open? return true/false
            * is the space horizontal or vertical? Needed to check the correct fence board.
            * is a fence in between horizontally or vertically? return true/false
            * is the move legal with jumping a pawn rule? return true/false for this special case.
        * make the move if the check returns true
            * clear the old position
            * Update the new position to coordinates save the old position for the next step
            * call is_winner() to check if the player won
            * end the turn
        """
        if self._move_check(player, coord):
            # Move my guy
            position_i = self.get_player_position(player)  # Record initial position
            self.set_player_board_space("□", position_i[0], position_i[1])  # Clear the starting position
            self.set_player_board_space(player, coord[0], coord[1])  # Place the player at the new position
            self.set_player_position(player, coord)  # Update the player_position
            self.is_winner(player)  # Check if the player won
            self.next_turn()  # End the turn

        else:
            return False  # The checks fails. Some part of the move is illegal

    def _check_fence_placement(self, direction: str, coord: tuple):
        """Checks if this position is legal for fence placement and returns true or false. uses direction and
        coordinate parameters
            * check the direction to get the correct wall board
            * check if the space is open
        """

        # Direction is validated during the coordinate check
        fence_board = None
        if direction == "h":
            fence_board = self.get_horizontal_wall_board()
        elif direction == "v":
            fence_board = self.get_vertical_wall_board()
        else:
            print("Something went wrong")
            return
        # Check that a path to the end remains todo
        if fence_board[coord[0]][coord[1]] == "  ":
            return True  # Space is open
        else:
            return False  # Space is not open

        print("Something went wrong in _check_fence_placement()")
        return False

    def _fence_coordinate_check(self, direction, coord):
        """Validates the direction and coordinates parameters and returns true if they are valid.
            * Check to make sure the direction is "v" or "h"
            * Check the coordinates are on the board"""
        fence_board = None
        if direction == "v":
            fence_board = self.get_vertical_wall_board()
        elif direction == "h":
            fence_board = self.get_vertical_wall_board()
        else:
            print("Invalid direction")
            return False

        if 0 > coord[0] or coord[0] >= len(fence_board):
            return False  # Coordinate is out of bounds
        elif 0 > coord[1] or coord[1] >= len(fence_board[0]):
            return False  # Coordinate is out of bounds
        else:
            return True

    def _set_fence_space(self, direction, coord):
        """Updates the fence board using direction parameters for the correct board and coord to know where to place
        the fence. This is called by place_fence() """
        if direction == "v":
            self._vertical_wall_board[coord[0]][coord[1]] = " |"
        elif direction == "h":
            self._horizontal_wall_board[coord[0]][coord[1]] = "__"
        else:
            print("Something went wrong in set_fence_space()")

    def _debug_fence_board(self, value, x, y, direction):
        """debug function of labeling each wall slot with it's coordinates.
        *pass
        """
        if direction == "h":
            self._horizontal_wall_board[x][y] = value
        if direction == "v":
            self._vertical_wall_board[x][y] = value

    def place_fence(self, player: int, direction: str, coord: tuple):
        """Placing a fence starts here. Takes a player int, direction string and coordinates as a tuple.
            *Check if it's the players turn using player parameters.
            *Check the player has fences left using player parameters.
            *Offset the coordinates to match the expected space for the Vertical or Horizontal board.
            *Call _fence_coordinate_check() to validate direction and coordinates as in range
            *Call _check_fence_placement() to make sure the space is open. if true:
                *_use_a_fences(player) to reduce the number of fences for player
                *_set_fence_space(to place the fence on the correct board at the coordinates.
                *next_turn() ends the turn
        """
        if self.get_turn() != player:
            print("Not your turn player", player)
            return False
        if self.get_fences_remaining(player) <= 0:
            print("Out of fences player", player)
            return False

        # Offset the position to match the wall boards
        if direction == "v":
            coord = (coord[0] - 1, coord[1])
        if direction == "h":
            coord = (coord[0], coord[1] - 1)

        if self._fence_coordinate_check(direction, coord) is False:
            print("Coordinates are out of bounds")
            return False

        if self._check_fence_placement(direction, coord):  # Check fence position is clear
            # Position is unoccupied
            self._use_a_fences(player)  # reduce number of fences
            self._set_fence_space(direction, coord)  # Place the fence
            self.next_turn()  # End Turn

    def is_winner(self, player):
        """This function will be called at the end of a player move to check if the player has won. It will check the
        y coordinate of the players new position to see if it is the opposite side. If the player won the game this
        function will disable future moves. I might just change the turn variable to "Game Over" as a easy way to make
        all the whose turn is it checks fail. it takes the player parameters """

        if player == 1:
            if self.get_player_position(player)[1] == 8:
                return True  # player 1 won
        elif player == 2:
            if self.get_player_position(player)[1] == 0:
                return True  # player 2 won


# some test code
game = QuoridorGame()
# game._debug_board_coord()

# game.print_board()
# game.move_pawn(1, (4, 1))
# game.print_board()
# game.place_fence(2, "h", (4, 2))
# game.print_board()
# game.move_pawn(1, (3, 1))
# game.print_board()
# game.place_fence(2, "v", (4, 5))
# game.print_board()
# game.move_pawn(1, (4, 1))
# game.print_board()
# game.place_fence(1, "v", (1, 2))
# game.print_board()
# game.place_fence(2, "v", (1, 3))
# game.print_board()
# game.place_fence(1, "v", (1, 4))
# game.print_board()
# game.place_fence(2, "v", (1, 5))
# game.print_board()
# game.place_fence(1, "v", (1, 6))
# game.print_board()
# game.place_fence(2, "v", (1, 7))
# game.print_board()
# game.place_fence(1, "v", (1, 8))
# game.print_board()
# game.place_fence(2, "v", (1, 8))
# game.print_board()
# game.place_fence(2, "v", (2, 3))
# game.place_fence(1, "v", (3, 3))
# game.place_fence(2, "v", (3, 4))
# game.place_fence(1, "v", (3, 5))
# game.place_fence(2, "v", (3, 6))
# game.print_board()
# input()
# game.place_fence(1, "v", (3, 7))
# game.print_board()
# input()
# game.place_fence(2, "v", (3, 8))
# game.place_fence(1, "v", (3, 9))
# game.place_fence(2, "v", (5, 5))
# game.print_board()
