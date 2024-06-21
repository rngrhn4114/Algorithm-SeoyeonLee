def solution(num_list):
    answer = 0
    even_number = ''
    odd_number = ''
    for i in num_list:
        if i % 2 == 0:
            even_number += str(i)
        else:
            odd_number += str(i)
    answer = int(even_number) + int(odd_number)
    return answer