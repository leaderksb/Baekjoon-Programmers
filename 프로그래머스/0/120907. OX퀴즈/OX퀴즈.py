def solution(quiz):
    answer = []
    
    for qu in quiz:
        q = qu.split()
        
        if q[1] == '-':
            if (int(q[0]) - int(q[2])) == int(q[4]):
                answer.append('O')
            else:
                answer.append('X')
        
        elif q[1] == '+':
            if (int(q[0]) + int(q[2])) == int(q[4]):
                answer.append('O')
            else:
                answer.append('X')
        
    return answer