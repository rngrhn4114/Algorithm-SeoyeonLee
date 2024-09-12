# collections 모듈에서 double-ended-queue(deque) 불러오기
# double-ended-queue는 양쪽에서 빠르게 데이터를 제거하거나 추가할 수 있다.
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 현재 다리 위 트럭 무게와 남은 이동 거리를 담을 큐 만들기
    bridge_queue = deque([0] * bridge_length)
    current_weight = 0  # 현재 다리 위 트럭들의 총 무게 초기화
    time = 0  # 건너는 시간 초기화

    # 트럭 무게나 현재 다리 위 트럭들의 총 무게가 0보다 크면 계속 반복
    while truck_weights or current_weight > 0:
        time += 1 # 한번 반복할 때마다 경과시간 1씩 늘리기
        
        # 다리에서 한 칸씩 트럭을 이동시키고(bridge_queue.popleft())
        # 다리에서 나간 트럭의 무게를 현재 다리 위 트럭들 무게에서 뺀다.
        current_weight -= bridge_queue.popleft()
        
        if truck_weights: # 다음 트럭이 존재할 때
            # 다음 트럭이 다리가 버티는 하중보다 합이 작으면
            if current_weight + truck_weights[0] <= weight:
                # 트럭을 truck_weights 에서 삭제한다.(다리 위에 올린다.)
                truck = truck_weights.pop(0)
                bridge_queue.append(truck)
                current_weight += truck
            else:
                # 트럭을 올릴 수 없으면 빈 칸을 추가한다.
                bridge_queue.append(0)

    return time