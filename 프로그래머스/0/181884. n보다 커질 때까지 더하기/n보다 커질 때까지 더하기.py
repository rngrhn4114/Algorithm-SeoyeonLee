def solution(numbers, n):
    answer = 0
    for i in numbers:
        if answer <= n:
            answer += i
        else:
            answer
    return answer