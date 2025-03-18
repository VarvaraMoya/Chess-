import copy


# Базовый класс шахматной фигуры
class ChessPiece:
    """Abstract base class for all chess pieces."""

    def __init__(self, color):
        """Initialize a chess piece with a given color.

        Args:
            color (str): The color of the piece ('white' or 'black').
        """
        self.color = color

    def get_valid_moves(self, board, position):
        """Get valid moves for the piece on the board from a given position.

        Args:
            board (list): The chess board as a 2D list.
            position (tuple): The current position of the piece as (row, col).

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """
        raise NotImplementedError

    def __str__(self):
        """Return a string representation of the chess piece.

        Returns:
            str: The symbol representing the piece.
        """
        return self.symbol


# Классические шахматы
class King(ChessPiece):
    """Class representing a King in classic chess."""

    symbol = {'white': 'K', 'black': 'k'}

    def __init__(self, color):
        """Initialize a King piece.

        Args:
            color (str): The color of the King ('white' or 'black').
        """
        super().__init__(color)
        self.symbol = King.symbol[color]


class Queen(ChessPiece):
    """Class representing a Queen in classic chess."""

    symbol = {'white': 'Q', 'black': 'q'}

    def __init__(self, color):
        """Initialize a Queen piece.

        Args:
            color (str): The color of the Queen ('white' or 'black').
        """
        super().__init__(color)
        self.symbol = Queen.symbol[color]


class Rook(ChessPiece):
    """Class representing a Rook in classic chess."""

    symbol = {'white': 'R', 'black': 'r'}

    def __init__(self, color):
        """Initialize a Rook piece.

        Args:
            color (str): The color of the Rook ('white' or 'black').
        """
        super().__init__(color)
        self.symbol = Rook.symbol[color]


class Bishop(ChessPiece):
    """Class representing a Bishop in classic chess."""

    symbol = {'white': 'B', 'black': 'b'}

    def __init__(self, color):
        """Initialize a Bishop piece.

        Args:
            color (str): The color of the Bishop ('white' or 'black').
        """
        super().__init__(color)
        self.symbol = Bishop.symbol[color]


class Knight(ChessPiece):
    """Class representing a Knight in classic chess."""

    symbol = {'white': 'N', 'black': 'n'}

    def __init__(self, color):
        """Initialize a Knight piece.

        Args:
            color (str): The color of the Knight ('white' or 'black').
        """
        super().__init__(color)
        self.symbol = Knight.symbol[color]


class Pawn(ChessPiece):
    """Class representing a Pawn in classic chess."""

    symbol = {'white': 'P', 'black': 'p'}

    def __init__(self, color):
        """Initialize a Pawn piece.

        Args:
            color (str): The color of the Pawn ('white' or 'black').
        """
        super().__init__(color)
        self.symbol = Pawn.symbol[color]


# Классическая шахматная доска
class ChessBoard:
    """Class representing a classic 8x8 chess board."""

    def __init__(self):
        """Initialize a new chess board with pieces in starting positions."""
        self.board = self.create_initial_board()
        self.move_history = []

    def create_initial_board(self):
        """Create the initial setup of the chess board.

        Returns:
            list: A 2D list representing the board with pieces placed.
        """
        board = [[None] * 8 for _ in range(8)]
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(8):
            board[0][i] = piece_order[i]('black')
            board[7][i] = piece_order[i]('white')
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')

        return board

    def display(self):
        """Display the current state of the chess board."""
        print("  A B C D E F G H")
        print("  ----------------")
        for i in range(8):
            row = str(8 - i) + " "
            for j in range(8):
                row += (str(self.board[i][j]) if self.board[i][j] else '.') + ' '
            print(row + str(8 - i))
        print("  ----------------")
        print("  A B C D E F G H")

    def move_piece(self, start, end):
        """Move a piece from start position to end position if valid.

        Args:
            start (tuple): Starting position as (row, col).
            end (tuple): Ending position as (row, col).
        """
        x1, y1 = start
        x2, y2 = end
        piece = self.board[x1][y1]
        if piece and self.is_valid_move(piece, start, end):
            self.move_history.append(copy.deepcopy(self.board))
            self.board[x2][y2] = piece
            self.board[x1][y1] = None
        else:
            print("Недопустимый ход! Попробуйте еще раз.")

    def is_valid_move(self, piece, start, end):
        """Check if a move is valid for the given piece.

        Args:
            piece (ChessPiece): The piece to move.
            start (tuple): Starting position as (row, col).
            end (tuple): Ending position as (row, col).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return True  # Здесь должна быть проверка допустимости хода по правилам шахмат

    def undo_move(self):
        """Undo the last move made on the board."""
        if self.move_history:
            self.board = self.move_history.pop()


class ChessGame:
    """Class managing a classic chess game."""

    def __init__(self):
        """Initialize a new chess game."""
        self.board = ChessBoard()
        self.turn = 'white'
        self.move_count = 0

    def switch_turn(self):
        """Switch the turn to the other player."""
        self.turn = 'black' if self.turn == 'white' else 'white'

    def play(self):
        """Run the main game loop for classic chess."""
        while True:
            self.board.display()
            print(f"Ход {self.move_count + 1}, {self.turn} ходит")
            start = input(f"{self.turn.capitalize()}, выберите фигуру (например, E2): ")
            end = input(f"{self.turn.capitalize()}, введите целевую позицию (например, E4): ")

            if start.lower() == 'undo' or end.lower() == 'undo':
                self.board.undo_move()
                self.switch_turn()
                continue

            try:
                x1, y1 = 8 - int(start[1]), ord(start[0].lower()) - ord('a')
                x2, y2 = 8 - int(end[1]), ord(end[0].lower()) - ord('a')
                self.board.move_piece((x1, y1), (x2, y2))
                self.switch_turn()
                self.move_count += 1
            except Exception as e:
                print("Неверный ввод! Попробуйте еще раз.")


# Гексагональные шахматы
class HexChessBoard:
    """Class representing a hexagonal chess board."""

    def __init__(self):
        """Initialize a new hexagonal chess board."""
        self.board = self.create_initial_board()
        self.move_history = []

    def create_initial_board(self):
        """Create the initial setup for a hexagonal chess board.

        Returns:
            list: A 2D list representing the hexagonal board with pieces.
        """
        board = [[None] * 11 for _ in range(11)]
        piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(8):
            board[0][i + 2] = piece_order[i]('black')
            board[10][i + 2] = piece_order[i]('white')
            board[1][i + 2] = Pawn('black')
            board[9][i + 2] = Pawn('white')

        return board

    def display(self):
        """Display the current state of the hexagonal chess board."""
        print("    A B C D E F G H I J K")
        for i in range(11):
            row = str(11 - i).rjust(2) + " "
            for j in range(11):
                row += (str(self.board[i][j]) if self.board[i][j] else '.') + ' '
            print(row + str(11 - i).rjust(2))
        print("    A B C D E F G H I J K")

    def move_piece(self, start, end):
        """Move a piece from start to end position if valid.

        Args:
            start (tuple): Starting position as (row, col).
            end (tuple): Ending position as (row, col).
        """
        x1, y1 = start
        x2, y2 = end
        piece = self.board[x1][y1]
        if piece and self.is_valid_move(piece, start, end):
            self.move_history.append(copy.deepcopy(self.board))
            self.board[x2][y2] = piece
            self.board[x1][y1] = None
        else:
            print("Недопустимый ход! Попробуйте еще раз.")

    def is_valid_move(self, piece, start, end):
        """Check if a move is valid for the given piece in hexagonal chess.

        Args:
            piece (ChessPiece): The piece to move.
            start (tuple): Starting position as (row, col).
            end (tuple): Ending position as (row, col).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return True  # Проверку ходов нужно доработать для гексагональных шахмат

    def undo_move(self):
        """Undo the last move made on the hexagonal board."""
        if self.move_history:
            self.board = self.move_history.pop()


class HexChessGame:
    """Class managing a hexagonal chess game."""

    def __init__(self):
        """Initialize a new hexagonal chess game."""
        self.board = HexChessBoard()
        self.players = ['white', 'black']
        self.turn_index = 0
        self.move_count = 0

    def switch_turn(self):
        """Switch the turn to the other player."""
        self.turn_index = (self.turn_index + 1) % 2

    def play(self):
        """Run the main game loop for hexagonal chess."""
        while True:
            self.board.display()
            current_player = self.players[self.turn_index]
            print(f"Ход {self.move_count + 1}, {current_player} ходит")
            start = input(f"{current_player.capitalize()}, выберите фигуру (например, E5): ")
            end = input(f"{current_player.capitalize()}, введите целевую позицию (например, E7): ")

            if start.lower() == 'undo' or end.lower() == 'undo':
                self.board.undo_move()
                self.switch_turn()
                continue

            try:
                x1, y1 = self.convert_to_coords(start)
                x2, y2 = self.convert_to_coords(end)
                self.board.move_piece((x1, y1), (x2, y2))
                self.switch_turn()
                self.move_count += 1
            except Exception as e:
                print("Неверный ввод! Попробуйте еще раз.")

    def convert_to_coords(self, position):
        """Convert a position string (e.g., 'E5') to board coordinates.

        Args:
            position (str): The position in format like 'E5'.

        Returns:
            tuple: The (row, col) coordinates on the board.
        """
        col = ord(position[0].lower()) - ord('a') + 1
        row = 11 - int(position[1:])
        return row, col


# Шашки
class CheckersPiece:
    """Class representing a piece in checkers."""

    def __init__(self, color, is_king=False):
        """Initialize a checkers piece.

        Args:
            color (str): The color of the piece ('white' or 'black').
            is_king (bool): Whether the piece is a king (default: False).
        """
        self.color = color
        self.is_king = is_king

    def promote(self):
        """Promote the piece to a king."""
        self.is_king = True

    def __str__(self):
        """Return a string representation of the checkers piece.

        Returns:
            str: The symbol representing the piece ('w', 'b', 'W', or 'B').
        """
        if self.is_king:
            return 'B' if self.color == 'black' else 'W'
        return 'b' if self.color == 'black' else 'w'


class CheckersBoard:
    """Class representing an 8x8 checkers board."""

    def __init__(self):
        """Initialize a new checkers board with pieces in starting positions."""
        self.board = self.create_initial_board()
        self.move_history = []

    def create_initial_board(self):
        """Create the initial setup of the checkers board.

        Returns:
            list: A 2D list representing the board with pieces placed.
        """
        board = [[None] * 8 for _ in range(8)]

        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 1:
                    board[i][j] = CheckersPiece('black')

        for i in range(5, 8):
            for j in range(8):
                if (i + j) % 2 == 1:
                    board[i][j] = CheckersPiece('white')

        return board

    def display(self):
        """Display the current state of the checkers board."""
        print("  A B C D E F G H")
        for i in range(8):
            row = str(8 - i) + " "
            for j in range(8):
                row += (str(self.board[i][j]) if self.board[i][j] else '.') + ' '
            print(row + str(8 - i))
        print("  A B C D E F G H")

    def move_piece(self, start, end):
        """Move a checkers piece from start to end position if valid.

        Args:
            start (tuple): Starting position as (row, col).
            end (tuple): Ending position as (row, col).
        """
        x1, y1 = start
        x2, y2 = end
        piece = self.board[x1][y1]
        if piece and self.is_valid_move(piece, start, end):
            self.move_history.append(copy.deepcopy(self.board))
            self.board[x2][y2] = piece
            self.board[x1][y1] = None

            if (piece.color == 'white' and x2 == 0) or (piece.color == 'black' and x2 == 7):
                piece.promote()
        else:
            print("Недопустимый ход! Попробуйте еще раз.")

    def is_valid_move(self, piece, start, end):
        """Check if a move is valid for the given checkers piece.

        Args:
            piece (CheckersPiece): The piece to move.
            start (tuple): Starting position as (row, col).
            end (tuple): Ending position as (row, col).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        x1, y1 = start
        x2, y2 = end
        dx, dy = x2 - x1, y2 - y1

        if self.board[x2][y2] is not None:
            return False

        if piece.is_king:
            return abs(dx) == abs(dy) in [1, 2]
        else:
            direction = -1 if piece.color == 'white' else 1
            if dx == direction and abs(dy) == 1:
                return True
            if dx == 2 * direction and abs(dy) == 2:
                mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
                if self.board[mid_x][mid_y] and self.board[mid_x][mid_y].color != piece.color:
                    self.board[mid_x][mid_y] = None  # Бьем шашку
                    return True
        return False

    def undo_move(self):
        """Undo the last move made on the checkers board."""
        if self.move_history:
            self.board = self.move_history.pop()


class CheckersGame:
    """Class managing a checkers game."""

    def __init__(self):
        """Initialize a new checkers game."""
        self.board = CheckersBoard()
        self.players = ['white', 'black']
        self.turn_index = 0

    def switch_turn(self):
        """Switch the turn to the other player."""
        self.turn_index = (self.turn_index + 1) % 2

    def play(self):
        """Run the main game loop for checkers."""
        while True:
            self.board.display()
            current_player = self.players[self.turn_index]
            print(f"{current_player.capitalize()} ходит")
            start = input(f"Выберите шашку (например, E3): ")
            end = input(f"Введите целевую позицию (например, F4): ")

            if start.lower() == 'undo' or end.lower() == 'undo':
                self.board.undo_move()
                self.switch_turn()
                continue

            try:
                x1, y1 = self.convert_to_coords(start)
                x2, y2 = self.convert_to_coords(end)
                self.board.move_piece((x1, y1), (x2, y2))
                self.switch_turn()
            except Exception:
                print("Неверный ввод! Попробуйте еще раз.")

    def convert_to_coords(self, position):
        """Convert a position string (e.g., 'E3') to board coordinates.

        Args:
            position (str): The position in format like 'E3'.

        Returns:
            tuple: The (row, col) coordinates on the board.
        """
        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])
        return row, col


# Меню выбора игры
def main():
    """Display a menu to select and start a game."""
    print("Выберите игру:")
    print("1. Классические шахматы")
    print("2. Гексагональные шахматы")
    print("3. Шашки")
    choice = input("Введите номер игры: ")

    if choice == '1':
        game = ChessGame()
        game.play()
    elif choice == '2':
        game = HexChessGame()
        game.play()
    elif choice == '3':
        game = CheckersGame()
        game.play()
    else:
        print("Неверный выбор. Завершение программы.")


if __name__ == "__main__":
    main()
