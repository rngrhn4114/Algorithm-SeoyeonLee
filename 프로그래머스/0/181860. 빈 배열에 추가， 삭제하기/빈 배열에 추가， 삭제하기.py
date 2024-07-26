def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == 1:
            for _ in range(2*arr[i]):
                answer.append(arr[i])
        elif flag[i] == 0:
            for _ in range(arr[i]):
                answer.pop(-1)
    return answer