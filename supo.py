one = [1,2,3,4,5]
two = [2,1,2,3,2,4,2,5]
three = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    points = [0, 0, 0]
    one_len = len(one)
    two_len = len(two)
    three_len = len(three)
    
    for i, an in enumerate(answers):
        if one[i%one_len] == an:
            points[0] += 1
            
        if two[i%two_len] == an:
            points[1] += 1
        
        if three[i%three_len] == an:
            points[2] += 1
            
    
    m = max(points)
    
    
    answer = []
    for i in range(3):
        if points[i] == m:
            answer.append(i+1)
    return answer



print(solution([1,3,2,4,2]))


