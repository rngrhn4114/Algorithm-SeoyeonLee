def solution(num_list, n):
    answer = []
    front = num_list[:n]
    back = num_list[n:]
    answer = back + front
    return answer