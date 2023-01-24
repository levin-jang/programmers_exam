def solution(k, dungeons):
    answer = 0
    dungeon_dict = {}
    for d in dungeons:
        dungeon_dict[d[0]] = d[1]

    print(dungeon_dict)

    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
