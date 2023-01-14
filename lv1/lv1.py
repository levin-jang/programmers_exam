

def solution(s, n):
    A = ord('A')
    Z = ord('Z')
    a = ord('a')
    z = ord('z')
    space =ord(' ')
    answer = ''
    
    for c in s:
        _c = ord(c)
        if _c == space:
            answer += chr(_c)
            continue
        
        _cn = _c + n
        
        if _c >= A and _c <= Z:
            if _cn > Z:
                _cn = A + _cn% Z -1
            # _cn = _cn % Z
            answer += chr(_cn)
            continue
        
        if _c >= a and _c<=z:
            if _cn > z:
                _cn = a + _cn% z -1
            answer += chr(_cn)
            continue
            
    return answer



print(solution('a B z', 4))

