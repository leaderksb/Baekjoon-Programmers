from math import prod

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    
    per_list = list(zip(A, B))
    
    answer = 0
    
    for p in per_list:
        answer += prod(p)

    return answer
