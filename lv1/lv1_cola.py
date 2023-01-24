def solution(a, b, n):
    answer = 0
    while n >= a:
        ret = (n // a) * b
        answer += ret
        n = ret + n % a
    return answer


print(solution(2, 1, 20))
