# Author: Cameron Bowers
# Date: 08/03/2021
# Description: This program is a game called quoridor

class QuoridorGame:
    """The Quoridor class contains everything needed to play the game"""

    def _generate_board(self):
        """This method is called by __init__ to generates a blank board. The blank board has 3 sub boards. One tracks
        the player positions. One tracks the Horizontal walls. one tracks vertical walls. each board is a list
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
         * Set the starting player positions.
         * Initialize the current turn to player 1 and track it's value as updated.
         * Initialize variable to track how many fences each player have remaining.
         """
        # Generate the boards
        self._player_board, self._vertical_wall_board, self._horizontal_wall_board = self._generate_board()

        # Set player starting positions
        self.set_player_board_space(1, 4, 0)
        self.set_player_board_space(2, 4, 8)

        self._turn = 1  # 1 is player 1, 2 is player 2

        # track number of fence each player has left
        self._player1_fences = 10
        self._player2_fences = 10

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

    def get_turn(self):
        """Return the current turn"""
        return self._turn

    def next_turn(self):
        """This method changes the turn to the other players turn. It will be called by placing a wall or moving a
        player """
        if self.get_turn() == 1:
            self._turn = 2
        elif self.get_turn() == 2:
            self._turn = 1

    def get_fences_remaining(self, player):
        """returns the number of fences the player has remaining. This method is used as a check in place_fence() to
        make sure the player has enough fences left. """
        if player == 1:
            return self._player1_fences
        elif player == 2:
            return self._player2_fences
        else:
            print("invalid player?")

    def _use_a_fences(self, player):
        """Reduces the fences remaining by 1 for player. This method is used at the conclusion of the place_fence()."""
        if player == 1:
            self._player1_fences -= 1
        elif player == 2:
            self._player2_fences -= 1
        else:
            print("invalid player?")

    def _composite_board(self):
        """The method is part of the print board process. It composites the player and wall boards in preparation to
        display a beautiful ascii board in the console. This function places ⚫ characters where walls can come
        together. The master board returned will be a list of lists."""
        master_board = []
        for x in range(len(self.get_player_board())):
            master_board.append(self.get_player_board()[x].copy())

        for x in range(len(self.get_horizontal_wall_board())):
            for y in range(len(self.get_horizontal_wall_board()[x])):
                master_board[x].insert(2 * y + 1, self.get_horizontal_wall_board()[x][y])

        for x in range(len(self.get_vertical_wall_board())):
            if x < len(self.get_vertical_wall_board()):
                master_board.insert(2 * x + 1, self.get_vertical_wall_board()[x].copy())
                for y in range(len(master_board[2 * x + 1]) - 1):
                    master_board[2 * x + 1].insert(-1 - 2 * y, "⚫")
        return master_board

    def print_board(self):
        """Prints the game board to console. To do this a list of 17 strings is made. Then we cycle through the
        master board we generated converting each list item in to a string. Because our master list is [x][y] we
        can't just print the list of list or the orientation will be wrong in the console. We reference each list item
        by coordinate to get them order."""

        print("________Current Board_________")
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
        """Replaces every player square with it's coordinates then prints. This method is used for debugging to verify
        which positions are which."""
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

        self.print_board()

    def move_pawn(self):
        """This function will move a pawn once it's finished. To do this,
        * check if the move is legal
            * is the space open,
            * is the space horizontal or vertical
            * is a fence in between horizontal of vertical
            * is the move legal with jumping a pawn rule


        """

    def _check_fence_placement(self, direction: str, coord: tuple):
        """Checks if this position is legal for fence placement"""

        # Direction is validated during the coordinate check
        fence_board = None
        if direction == "h":
            fence_board = self.get_horizontal_wall_board()
        elif direction == "v":
            fence_board = self.get_vertical_wall_board()
        else:
            print("Something went wrong")
            return
        if fence_board[coord[0]][coord[1]] == "  ":
            return True  # Space is open
        else:
            return False  # Space is not open

        print("Something went wrong in _check_fence_placement()")
        return False

        # Check that a path to the end remains todo
    def _fence_coordinate_check(self, direction, coord):
        """Validates the direction and coordinates"""
        fence_board = None
        if direction == "v":
            fence_board = self.get_vertical_wall_board()
        elif direction == "h":
            fence_board = self.get_vertical_wall_board()
        else:
            print("Invalid direction")
            return False

        if 0 > coord[0] or coord[0] >= len(fence_board):
            return False # Coordinate is out of bounds
        elif 0 > coord[1] or coord[1] >= len(fence_board[0]):
            return False # Coordinate is out of bounds
        else:
            return True

    def _set_fence_space(self, direction, coord):
        """Updates the fence board"""
        if direction == "v":
            self._vertical_wall_board[coord[0]][coord[1]] = " |"
        elif direction == "h":
            self._horizontal_wall_board[coord[0]][coord[1]] = "__"
        else:
            print("Something went wrong in set_fence_space()")

    def _debug_fence_board(self, value, x, y, direction):
        """debug function of labeling each wall slot with it's coordinates."""
        if direction == "h":
            self._horizontal_wall_board[x][y] = value
        if direction == "v":
            self._vertical_wall_board[x][y] = value

    def place_fence(self, player: int, direction: str, coord: tuple):
        """Placing a fence starts here"""
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


game = QuoridorGame()
# game._debug_board_coord()

game.print_board()
game.place_fence(1, "v", (7, 0))
game.print_board()
game.place_fence(2, "v", (1, 0))
game.print_board()
game.place_fence(1, "v", (1, 2))
game.print_board()
game.place_fence(2, "v", (1, 3))
game.print_board()
game.place_fence(1, "v", (1, 4))
game.print_board()
game.place_fence(2, "v", (1, 5))
game.print_board()
game.place_fence(1, "v", (1, 6))
game.print_board()
game.place_fence(2, "v", (1, 7))
game.print_board()
game.place_fence(1, "v", (1, 8))
game.print_board()
game.place_fence(2, "v", (1, 8))
game.print_board()
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
