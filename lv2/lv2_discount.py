def solution(want, number, discount):
    answer = 0
    want_number = dict(zip(want, number))
    discount_10day = {}
    for i, dis in enumerate(discount):
        if i < 9:
            if dis in discount_10day.keys():
                discount_10day[dis] += 1
            else:
                discount_10day[dis] = 1
            continue

        if dis in discount_10day.keys():
            discount_10day[dis] += 1
        else:
            discount_10day[dis] = 1

        good = True
        for key, value in want_number.items():
            if key not in discount_10day.keys():
                good = False
                break
            else:
                if discount_10day[key] != value:
                    good = False
        if good:
            answer += 1

        remove = discount[i - 9]
        discount_10day[remove] -= 1
        if discount_10day[remove] == 0:
            del discount_10day[remove]

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = [
    "chicken",
    "apple",
    "apple",
    "banana",
    "rice",
    "apple",
    "pork",
    "banana",
    "pork",
    "rice",
    "pot",
    "banana",
    "apple",
    "banana",
]

print(solution(want, number, discount))
