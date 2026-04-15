class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Thinking brute force
        # Step 1: Go through each row first and check for duplicates, if found return false else move to step 2
        # Step 2: Go through each column and check for duplicates, if found return false else move to step 3
        # Step 3: Check each 3 * 3 sub boxes and check for duplicates, if found return false else return true
        
        # Step 1: Check the rows
        for i in range(len(board)):
            row_duplicates = {}
            row = board[i]
            for j in range(len(row)):
                if row[j] == ".":
                    continue
                if row[j] in row_duplicates:
                    return False
                row_duplicates[row[j]] = 1
        
        # Step 2: Check the columns
        for i in range(9):
            col_duplicates = {}
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if val in col_duplicates:
                    return False
                col_duplicates[val] = 1

        # Step 3: Check the sub-boxes
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True


        