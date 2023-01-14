def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:
        [t, months] = term.split()
        term_dict[t] = int(months)

    print(term_dict)
    for i, pri in enumerate(privacies):
        [date, t] = pri.split()
        # print("original :", date)
        [y, m, d] = date.split(".")

        _m = int(m) + term_dict[t]

        _y = int(y) + _m // 12
        _m = _m % 12

        expired_date = f"{_y}.{_m:02d}.{d}"
        if today > expired_date:
            # print(f"{today}, {expired_date}")
            answer.append(i + 1)

        # print("expired :", expired_date)
    return answer


today = "2020.01.01"
terms = ["Z 3", "D 5"]

privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today, terms, privacies))
