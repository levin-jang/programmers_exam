def solution(s):
    answer = 0
    fc = 0
    nc = 0
    f = ""
    an = ""
    for c in s:
        if f == "":
            f = c
            fc += 1
            an = c
            continue

        if f == c:
            fc += 1
        else:
            nc += 1
        an += c

        if fc == nc:
            # print(an)
            fc = 0
            nc = 0
            f = ""
            answer += 1

    if fc > 0:
        # print(an)
        answer += 1

    return answer


s = "aaabbaccccabba"
print(solution(s))
