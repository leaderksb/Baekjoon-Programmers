def solution(s):
    answer = ''
    
    s_list = s.split(' ')
    
    for c in s_list:
        answer += c.capitalize() + ' '
    
    return answer[0:-1]