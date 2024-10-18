def solution(s):
    num = int(len(s))
    
    # 홀수일 때
    if num % 2 == 1:
        return s[num // 2]
    # 짝수일 때
    else:
        return s[num // 2 - 1:num // 2 + 1]