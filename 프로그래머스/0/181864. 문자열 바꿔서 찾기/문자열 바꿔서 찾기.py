def solution(myString, pat):
    answer = 0
    myString1 = myString.replace("A", "b").replace("B", "A")
    if pat in myString1.upper():
        answer = 1
    return answer