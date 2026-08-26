class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]
        

        for i in range(9): 
            for j in range(9): 
                if board[i][j].isdigit(): 
                    if board[i][j] not in row[i]: 
                        row[i].add(board[i][j])
                    else: 
                        return False 
                    
                    if board[i][j] not in col[j]: 
                        col[j].add(board[i][j])
                    else: 
                        return False 

                    box_i = (i // 3) * 3 + (j // 3)
                    if board[i][j] not in box[box_i]: 
                        box[box_i].add(board[i][j])
                    else: 
                        return False 

        return True

        