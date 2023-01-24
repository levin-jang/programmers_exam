def solution(weights):
    answer = 0

    ratio = [1 / 1, 2 / 3, 2 / 4, 3 / 2, 3 / 4, 4 / 2, 4 / 3]
    counts = {}
    for i in weights:
        counts[i] = counts.get(i, 0) + 1

    nums = list(counts.keys())

    for n in nums:
        c = counts[n]
        answer += c * (c - 1) // 2

    for fi, fn in enumerate(nums[:-1]):
        for si, sn in enumerate(nums[fi + 1 :]):
            divide = fn / sn
            if divide in ratio:
                answer += counts[fn] * counts[sn]
    return answer


weights = [100, 100, 100, 100, 200, 200]
print(solution(weights))
