def solution(my_string, is_prefix):
    answer = 0
    if is_prefix in my_string:
        if is_prefix[0] == my_string[0] and is_prefix[1] == my_string[1]:
            answer = 1
    return answer