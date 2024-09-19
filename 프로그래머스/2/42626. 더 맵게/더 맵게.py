import heapq

def solution(scoville, K):
    # scoville을 최소 힙 구조로 변환하기 (가장 작은 원소가 맨 앞에 오게 한다.)
    heapq.heapify(scoville)
    count = 0
    
    # 가장 작은 원소를 꺼내기
    spicy = heapq.heappop(scoville)
    
    # 가장 작은 스코빌 지수가 K보다 낮을 경우 계속해서 반복
    while spicy < K:
        try:
            # 두 번째로 작은 원소를 꺼내 첫 번째 원소와 섞기
            # 새로운 스코빌 지수는 (가장 작은 원소) + (두 번째로 작은 원소 * 2)
            new_spicy = spicy + (heapq.heappop(scoville) * 2)
        except:
            # 만약 두 번째 원소를 꺼낼 수 없다면 (리스트가 비었을 때), -1 반환
            return -1
        
        # 섞은 후의 새로운 스코빌 지수(new_spicy)를 힙에 다시 추가하기
        heapq.heappush(scoville, new_spicy)
        
        # 다음 섞기을 위해 가장 작은 원소를 다시 꺼냄
        spicy = heapq.heappop(scoville)
        
        # 섞은 횟수를 1 증가시키기
        count += 1

    return count