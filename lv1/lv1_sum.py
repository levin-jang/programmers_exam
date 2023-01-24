def solution(a, b):
    aa = 0
    bb = 0
    if a > 0:
        aa = a * (a + 1) / 2
    else:
        aa = a * (a - 1) / -2

    if b > 0:
        bb = b * (b + 1) / 2
    else:
        bb = b * (b - 1) / -2
    answer = 0

    if (aa < 0 and bb > 0) or (aa > 0 and bb < 0):
        answer = aa + bb

    if (aa > 0 and bb > 0) or (aa < 0 and bb < 0):
        if aa > bb:
            answer = aa - bb + b
        else:
            answer = bb - aa + a

    if aa < 0 and bb < 0:
        if aa < bb:
            answer = aa - bb + b
        else:
            answer = bb - aa + a

    return int(answer)


print(solution(-5, -3))
