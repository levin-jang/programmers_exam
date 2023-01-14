def solution(board):
    answer = 1

    length = len(board)
    
    for ri in range(length):
        for ci in range(length):
            print(ri, ci, board[ri][ci])
        
        
    

    return answer

input = [
    [0,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [0,0,1,0]
    ]

print(solution(input))