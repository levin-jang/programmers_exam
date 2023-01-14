def solution1(t, p):
    p_l = len(p)
    t_l = len(t)
    # print(t_l, p_l)
    pi = int(p)
    answer = 0
    for i in range(t_l - p_l + 1):
        if int(t[i:i+p_l]) <= pi:
            answer += 1
        # print(t[i:i+p_l])
    return answer


def solution2(s):
    answer = []
    
    index_dict = {}
    for i, c in enumerate(s):
        if c in index_dict.keys():
            answer.append(i - index_dict[c])
        
        else:
            answer.append(-1)
        # print(i, c)
        index_dict[c] = i
    return answer


def solution3(storey):
    answer = 0
    while storey > 0:
        one = storey % 10
        storey = storey // 10
        if one > 5:
            answer += 10 - one
            storey += 1
        elif one == 5:
            if storey % 10 >= 5:
                storey += 1
            answer += one
        else:
            answer += one

    return answer

def solution(k, m, score: list):
    answer = 0
    score.sort(reverse=True)
    # print(score)
    for i in range(m -1, len(score), m):
        answer += (m * score[i])
        # print(i, score[i])
        
    
    return answer

print(solution(4, 3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2] ))

