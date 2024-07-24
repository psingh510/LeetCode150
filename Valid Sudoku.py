board = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
chk = True
# checking rows
for i in board:
    l = ['1','2','3','4','5','6','7','8','9']
    for j in range(len(i)): 
        if i[j] == ".":
            continue
        else:
            if i[j] in l:
                l.remove(i[j])
            else:
                chk = False
                break
# checking columns
for i in range(len(board)):
    l = ['1','2','3','4','5','6','7','8','9']
    for j in board: 
        if j[i] == ".":
            continue
        else:
            if j[i] in l:
                l.remove(j[i])
            else:
                chk = False
                break

for i in range(0,9):
    row_var = i/3
    col_var = i%3
    l = ['1','2','3','4','5','6','7','8','9']
    for i in range(3*int(row_var),(3*int(row_var))+3,1):
        for j in range(3*int(col_var),(3*int(col_var))+3,1):
            if board[i][j] == ".":
                continue
            else:
                if board[i][j] in l:
                    l.remove(board[i][j])
                else:
                    chk = False
                    break
            
print(chk)      
    