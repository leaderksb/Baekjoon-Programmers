from itertools import *

def solution(number):
    answer = 0
    
    for p in combinations(number, 3):
        if sum(p) == 0:
            answer += 1
    
    return answer