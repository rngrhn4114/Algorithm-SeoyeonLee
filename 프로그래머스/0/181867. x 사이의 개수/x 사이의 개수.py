def solution(myString):
    answer = []
    nanum = myString.split('x')
    for i in nanum:
        answer.append(len(i))
    return answer