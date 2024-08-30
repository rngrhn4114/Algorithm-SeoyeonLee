def solution(nums):
    answer = 0
    num1 = len(nums)/2
    num2 = len(set(nums))
    answer = min(num1, num2)
    return answer