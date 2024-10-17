def solution(arr):
    start = -1
    answer = []
    
    for a in arr:
        if a != start:
            answer.append(a)
            start = a
            
    return answer