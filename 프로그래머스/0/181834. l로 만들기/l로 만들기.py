def solution(myString):
    answer = ''
    for i in myString:
        if i > 'l':
            answer += i
        else:
            answer += 'l'
    return answer