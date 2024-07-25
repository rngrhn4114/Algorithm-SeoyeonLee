def solution(myString):
    answer = []
    answer = sorted(filter(None, myString.split('x')))
    return answer