def solution(arr, intervals):
    answer = []
    for a1, b1 in intervals:
        answer += arr[a1:b1+1]
    return answer