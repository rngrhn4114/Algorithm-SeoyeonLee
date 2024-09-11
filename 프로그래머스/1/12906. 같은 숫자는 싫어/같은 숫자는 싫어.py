def solution(arr):
    answer = []
    answer.append(arr[0]) # 가장 첫번째 원소 미리 저장해놓기
    
    # index 1인 요소부터 시작해서 다르면 arr[i] 추가하기
    # 만약 arr[i-1] 를 추가한다고 작성하면 실패이다.
    # 왜냐하면 이미 0번째 인덱스의 요소를 추가하였기 때문에 만약 1번째 인덱스의 요소가
    # 연속하는 같은 수였거나 연속하지 않는 수였더라도 첫번쨰 원소를 추가하게 되는 것이기 때문
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])  
    return answer 