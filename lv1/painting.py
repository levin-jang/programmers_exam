def solution(n, m, section):
    answer = 0
    paint = 0
    for s in section:
        if paint < s:
            answer += 1
            paint = s + m - 1
        # print(s)
    return answer


print(solution(4, 1, [1, 2, 3, 4]))
