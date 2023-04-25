def solution(players, callings):
    answer = list()
    rank = {}
    reverse = {}

    for i, player in enumerate(players):
        rank[player] = i
        reverse[i] = player

    for call in callings:
        r = rank[call]
        p = reverse[r - 1]
        rank[call] = r - 1
        rank[p] = r
        reverse[r - 1] = call
        reverse[r] = p

    for i in range(len(players)):
        answer.append(reverse[i])

    return answer


answer = solution(
    ["mumu", "soe", "poe", "kai", "mine"],
    ["kai", "kai", "mine", "mine"],
)

print(answer)
