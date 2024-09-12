# collections 모듈에서 deque 불러오기
from collections import deque

def solution(prices):
    # prices 리스트를 deque로 변환하기
    queue = deque(prices)
    answer = []
    
    # 큐가 비어있지 않을 때까지 반복하도록 한다.
    while queue:
        # 큐에서 첫 번째 요소(0번째 인덱스의 value)를 꺼내서 현재 가격으로 설정
        price = queue.popleft()
        # 현재 가격이 떨어지기까지 걸린 초 초기화
        sec = 0
        
        # 큐에 남아 있는 가격들을 순회
        for q in queue:
            sec += 1  # 1번 반복할때마다 시간 1초 늘어남.
            if price > q:
                # 현재 가격이 다음 가격보다 크면, 가격이 떨어진 것이므로 반복 탈출
                break
        
        # 현재 가격이 떨어지기까지 걸린 초를 결과 리스트에 추가한다.
        answer.append(sec)
    return answer
