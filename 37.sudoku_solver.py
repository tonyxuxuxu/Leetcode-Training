"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1


    def solve(self):
        row, col = self.findUnassigned()
        if row == -1 and col == -1:
            return True
        for num in ['1','2', '3', '4', '5', '6', '7', '8', '9']:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def isSafe(self, row, col, num):
        baserow = row - row % 3
        basecol = col - col % 3
        return self.checkRow(row, num) and self.checkCol(col, num) and self.checkSquare(baserow, basecol, num)

    def checkRow(self, row, num):
        for col in range(9):
            if self.board[row][col] == num:
                return False
        return True

    def checkCol(self, col, num):
        for row in range(9):
            if self.board[row][col] == num:
                return False
        return True

    def checkSquare(self, row, col, num):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == num:
                    return False
        return True



