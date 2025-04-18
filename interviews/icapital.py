"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row 
and maximum in its column.

DISTINCT NUMBERS, in random positions based on their values, filled matrix, all positive integers


Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the 
maximum in its column.

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the 
maximum in its column.


"""

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        # matrix = [[3,7,8],[9,11,13],[15,16,17]]
        # matrix = [[7,8],[1,2]]
        m = len(matrix)
        n = len(matrix[0])
        
        lucky_numbers = []
        
        possible_row_numbers = [float("inf")] * m # [3, 9, 15]
        possible_column_numbers = [float("-inf")] * n # [15, 16, 17]
        
        # rows
        for x in range(m):
            # current_min_row = float("inf")
            for y in range(n):
                if matrix[x][y] < possible_row_numbers[x]:
                    possible_row_numbers[x] = matrix[x][y]
                
        # columns
        for y in range(n):
            for x in range(m):
                if matrix[x][y] > possible_column_numbers[y]:
                    possible_column_numbers[y] = matrix[x][y]
                    
        for num in possible_column_numbers:
            if num in possible_row_numbers:
                lucky_numbers.append(num)
        
        return lucky_numbers
        
        
        
print(Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]) == [15])
print(Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]) == [12])
     
        
# time complexity: O(n)
# space complexity: O(n)
        
        
        
        
        
        

