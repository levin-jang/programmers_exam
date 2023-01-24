def solution(k, score):
    answer = []
    top_k = []
    for s in score:
        if len(top_k) < k:
            top_k.append(s)
        else:
            last = min(top_k)
            if last < s:
                top_k.remove(last)
                top_k.append(s)

        answer.append(min(top_k))
    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
