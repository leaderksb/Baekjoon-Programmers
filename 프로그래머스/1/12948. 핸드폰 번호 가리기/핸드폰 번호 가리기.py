def solution(phone_number):
    num = len(phone_number) - 4
    star = '*' * num
    answer = star + phone_number[-4:]
    
    return answer