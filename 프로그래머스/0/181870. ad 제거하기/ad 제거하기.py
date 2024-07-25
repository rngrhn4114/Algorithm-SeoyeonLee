def solution(strArr):
    answer = []
    discard = []
    for i in strArr:
        if 'ad' in i:
            discard.append(i)
        else:
            answer.append(i)
    return answer