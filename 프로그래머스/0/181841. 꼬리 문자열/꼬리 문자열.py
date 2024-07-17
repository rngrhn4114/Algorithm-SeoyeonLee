def solution(str_list, ex):
    answer = ''
    discard = ''
    for i in str_list:
        if ex in i:
            discard += i
        else:
            answer += i
    return answer