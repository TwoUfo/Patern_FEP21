from abc import ABC, abstractmethod
from typing import List

class MoveRule(ABC):
    def __init__(self, position: List[int]):
        self.position = position

    @abstractmethod
    def get_all_moves(self) -> List[List[int]]:
        pass

class Piece:
    def __init__(self, position: List[int], color: str):
        self.position = position
        self.color = color
        self.number_of_moves = 0
        self.move_rule = None

    def move(self, new_position: List[int]) -> dict:
        moves = self.move_rule.get_all_moves()
        if new_position in moves:
            self.position = new_position
            self.number_of_moves += 1
            return {"message": "Move successful"}
        else:
            return {"message": "Invalid move"}

    @staticmethod
    def check_position_range(position: List[int]):
        x, y = position
        return 1 <= x <= 8 and 1 <= y <= 8

    def print_info(self) -> None:
        print(self.__str__())

    def __str__(self):
        return f"Piece: {self.__class__.__name__}, Color: {self.color}, Position: {self.position}, Moves: {self.number_of_moves}"

class PawnMove(MoveRule):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        moves = []
        moves.append((x + 1, y))

        if x == 2:
            moves.append((x + 2, y))

        moves.append((x + 1, y + 1))
        moves.append((x + 1, y - 1))

        valid_moves = [move for move in moves if Piece.check_position_range(move)]

        return valid_moves


class QueenMove(MoveRule):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        possible_moves = []

        for i in range(1, 8):
            if Piece.check_position_range((x + i, y)):
                possible_moves.append((x + i, y))
            else:
                break

        for i in range(1, 8):
            if Piece.check_position_range((x - i, y)):
                possible_moves.append((x - i, y))
            else:
                break

        for i in range(1, 8):
            if Piece.check_position_range((x, y + i)):
                possible_moves.append((x, y + i))
            else:
                break

        for i in range(1, 8):
            if Piece.check_position_range((x, y - i)):
                possible_moves.append((x, y - i))
            else:
                break

        for i in range(1, 8):
            move = (x + i, y + i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        for i in range(1, 8):
            move = (x + i, y - i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        for i in range(1, 8):
            move = (x - i, y + i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        for i in range(1, 8):
            move = (x - i, y - i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        return possible_moves

class KnightMove(MoveRule):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        possible_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2),
        ]

        valid_moves = [move for move in possible_moves if Piece.check_position_range(move)]

        return valid_moves


class BishopMove(MoveRule):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        possible_moves = []

        for i in range(1, 8):
            move = (x + i, y + i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        for i in range(1, 8):
            move = (x + i, y - i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        for i in range(1, 8):
            move = (x - i, y + i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        for i in range(1, 8):
            move = (x - i, y - i)
            if not Piece.check_position_range(move):
                break
            possible_moves.append(move)

        return possible_moves

class KingMove(MoveRule):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        possible_moves = [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x + 1, y - 1),
            (x - 1, y + 1), (x - 1, y - 1),
        ]
        valid_moves = [move for move in possible_moves if Piece.check_position_range(move)]

        return valid_moves

class RookMove(MoveRule):
    def get_all_moves(self) -> List[List[int]]:
        x, y = self.position
        possible_moves = []

        # Horizontal
        for i in range(1, 8):
            if Piece.check_position_range((x + i, y)):
                possible_moves.append((x + i, y))
            else:
                break

        for i in range(1, 8):
            if Piece.check_position_range((x - i, y)):
                possible_moves.append((x - i, y))
            else:
                break

        # Vertical
        for i in range(1, 8):
            if Piece.check_position_range((x, y + i)):
                possible_moves.append((x, y + i))
            else:
                break

        for i in range(1, 8):
            if Piece.check_position_range((x, y - i)):
                possible_moves.append((x, y - i))
            else:
                break

        return possible_moves


class Knight(Piece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = KnightMove(position)

class Bishop(Piece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = BishopMove(position)

class King(Piece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = KingMove(position)

class Rook(Piece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = RookMove(position)

class Queen(Piece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = QueenMove(position)

class Pawn(Piece):
    def __init__(self, position: List[int], color: str):
        super().__init__(position, color)
        self.move_rule = RookMove(position)
