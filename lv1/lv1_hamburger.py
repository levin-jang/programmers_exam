


def solution(ingredient:list):
    answer = 0
    table = []
    
    for m in ingredient:
        if len(table) < 3:
            table.append(m)
            continue
            
        if m != 1:
            table.append(m)
            continue
        
        if table[-1] != 3:
            table.append(m)
            continue
        
        if table[-2] != 2:
            table.append(m)
            continue
        
        if table[-3] != 1:
            table.append(m)
            continue
        
        table.pop()
        table.pop()
        table.pop()
        answer += 1
    
    return answer



print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))

