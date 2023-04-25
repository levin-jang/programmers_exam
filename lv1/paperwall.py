def solution(wallpaper):
    # left, top, right, bottom
    answer = [len(wallpaper), len(wallpaper[0]), 0, 0]
    for ri, row in enumerate(wallpaper):
        for ci, f in enumerate(row):
            if f == "#":
                # left

                if answer[1] > ci:
                    answer[1] = ci
                # top

                if answer[0] > ri:
                    answer[0] = ri
                # right

                if answer[3] < ci + 1:
                    answer[3] = ci + 1
                # bottom

                if answer[2] < ri + 1:
                    answer[2] = ri + 1
                # print(answer)
    return answer


print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
print(solution(["..", "#."]))
