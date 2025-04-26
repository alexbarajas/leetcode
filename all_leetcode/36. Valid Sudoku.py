"""
LeetCode Problem: 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/
Difficulty: Medium
Topics: Hash Table, Matrix
"""

import collections
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    n = 9
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row in range(n):
        for column in range(n):
            space = board[row][column]
            if space == ".":
                continue
            if space in rows[row] or space in columns[column] or space in squares[row // 3, column // 3]:
                return False
            rows[row].add(space)
            columns[column].add(space)
            squares[(row // 3, column // 3)].add(space)

    return True


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print(not isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
