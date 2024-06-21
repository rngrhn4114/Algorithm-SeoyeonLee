def solution(num_list):
    answer = 0
    mul = 1
    sum_list = 0
    
    for i in num_list:
        mul = mul * i
        sum_list = sum_list + i
        if mul < sum_list**2:
            answer = 1
        else:
            answer = 0
    return answer