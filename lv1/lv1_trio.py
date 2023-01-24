def solution(number: list):
    # print(number[:-1])
    answer = 0

    for i, ni in enumerate(number[:-2]):
        # print(ni)
        for j, nj in enumerate(number[i + 1 : -1]):
            # print(nj)
            for k, nk in enumerate(number[i + j + 2 :]):
                if 0 == ni + nj + nk:
                    answer += 1
    return answer


print(solution([-2, 3, 0, 2, -5]))
