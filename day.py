days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
months = [31,29,31,30,31,30,31,31,30,31,30,31]
def solution(a, b):
    m = 4 + b
    for i in range(a -1 ):
        m += months[i]
    
    
    return days[m % 7]



print(solution(5,24))