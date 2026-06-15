class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            cnt = {}
            for num in row:
                if num == ".":
                    continue

                elif num in cnt:
                    cnt[num] += 1
                else:
                    cnt[num] = 1
            
            for key, freq in cnt.items():
                if freq > 1:
                    return False

        for j in range(9):
            cnt1 = {}
            for i in range(9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in cnt1:
                    cnt1[board[i][j]] += 1
                else:
                    cnt1[board[i][j]] = 1
            
            for key, freq in cnt1.items():
                if freq > 1:
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                cnt2 = {}

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] in cnt2:
                            cnt2[board[r][c]] += 1
                        else:
                            cnt2[board[r][c]] = 1
                for key, value in cnt2.items():
                    if value > 1:
                        return False
        
        return True