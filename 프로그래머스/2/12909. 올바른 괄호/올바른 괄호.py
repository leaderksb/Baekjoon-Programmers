def solution(s):
    answer = True
    cnt = 0
    
    for c in s:
        if c=='(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            answer = False
    
    if cnt > 0:
        answer = False
        
    return answer