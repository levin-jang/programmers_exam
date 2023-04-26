def solution(s):
    answer = 0
    n = 0
    x = 0
    f = ""
    for c in s:
        if f == "":
            f = c
            n = 1
            continue

        if f == c:
            n += 1
        else:
            x += 1

        if n == x:
            answer += 1
            f = ""
            n = 0
            x = 0

    return answer


print(solution("aaabbaccccabba"))
