# Author: Cameron Bowers
# Date: 08/03/2021
# Description:todo

class QuoridorGame:
    """todo"""

    def _generate_board(self):
        """Generates a blank board"""
        y_player_row = []
        for i in range(9):
            y_player_row.append("□")
        x_player_row = []
        for i in range(9):
            x_player_row.append(y_player_row.copy())

        vertical_y_wall_row = []
        for i in range(8):
            vertical_y_wall_row.append("  ")

        vertical_x_wall_row = []
        for i in range(9):
            vertical_x_wall_row.append(vertical_y_wall_row.copy())

        horizontal_y_wall_row = []
        for i in range(9):
            horizontal_y_wall_row.append("  ")

        horizontal_x_wall_row = []
        for i in range(8):
            horizontal_x_wall_row.append(horizontal_y_wall_row.copy())

        return x_player_row, vertical_x_wall_row, horizontal_x_wall_row

    def __init__(self):
        """Initialize variables"""
        # Generate the boards
        self._player_board, self._vertical_wall_board, self._horizontal_wall_board = self._generate_board()

        # Set player starting positions
        self.set_player_board_space(1, 4, 0)
        self.set_player_board_space(2, 4, 8)

        self._turn = 1  # 1 is player 1, 2 is player 2

        # track number of fence each player has left
        self._player1_fences = 10
        self._player2_fences = 10

        self._master_board = self.composite_board()

    def get_player_board(self):
        """Returns the player board"""
        return self._player_board

    def set_player_board_space(self, value, x, y):
        """sets a space on the player board"""
        self._player_board[x][y] = value

    def get_vertical_wall_board(self):
        """Returns the vertical wall board"""
        return self._vertical_wall_board

    def get_horizontal_wall_board(self):
        """Return the Horizontal wall board"""
        return self._horizontal_wall_board

    def get_master_board(self):
        """Returns the master board"""
        return self._master_board

    def composite_board(self):
        """composites the player and wall boards"""
        master_board = self.get_player_board()

        for i in range(len(self.get_vertical_wall_board())):

            for n in range(len(self.get_vertical_wall_board()[i])):
                master_board[i].insert(2 * n + 1, self.get_vertical_wall_board()[i][n])
        for i in range(len(self.get_horizontal_wall_board())):
            if i < len(self.get_horizontal_wall_board()):
                master_board.insert(2 * i + 1, self.get_horizontal_wall_board()[i])
                for n in range(len(master_board[2 * i + 1]) - 1):
                    master_board[2 * i + 1].insert(-1 - 2 * n, "⚫")
        return master_board

    def print_board(self):
        """Prints the game board to console"""

        master_board = self.get_master_board()
        for i in range(len(master_board)):
            concatenated_line = ""
            for n in range(len(master_board[i])):
                concatenated_line += str(master_board[i][n])
            print(concatenated_line)

    def move_pawn(self):
        """todo"""

    def _check_fence_placement(self, direction: str, coord: tuple):
        """Checks if this position is legal for fence placement"""
        if direction != "h" and direction != "v":
            print("Direction is not 'h' or 'v'")
            return False

        if direction == "h":
            if coord[0] < 0 or len(self.get_horizontal_wall_board()) < coord[0] or coord[1] < 0 or len(
                    self.get_horizontal_wall_board()[0]) < coord[1]:
                return False  # Coordinate is out of bounds
            if self.get_horizontal_wall_board()[coord[0]][coord[1]] == "  ":
                return True  # Space is open
            else:
                return False  # Space is not open
        elif direction == "v":
            if coord[0] < 0 or len(self.get_vertical_wall_board()) < coord[0] or coord[1] < 0 or len(
                    self.get_vertical_wall_board()[0]) < coord[1]:
                return False  # Coordinate is out of bounds
            if self.get_vertical_wall_board()[coord[0]][coord[1]] == "  ":
                return True  # Space is open
            else:
                return False  # Space is not open

        print("Something went wrong in _check_fence_placement()")
        return False

        # Check that a path to the end remains

    def set_fence_space(self, direction, coord):
        """Updates the fence board"""
        if direction == "v":
            self._vertical_wall_board[coord[0]][coord[1]] = "| "
        elif direction == "h":
            self._horizontal_wall_board[coord[0]][coord[1]] = "__"
        else:
            print("Something went wrong in set_fence_space()")

    def place_fence(self, player: int, direction: str, coord: tuple):
        """Places a fence"""
        if self._check_fence_placement(direction, coord):
            # Position is unoccupied
            self.set_fence_space(direction, coord)

        # Check fence position is clear
        # reduce number of fences
        # Place the fence
        # End turn


game = QuoridorGame()
game.print_board()
game.place_fence(1, "v", (1, 0))
game.print_board()
