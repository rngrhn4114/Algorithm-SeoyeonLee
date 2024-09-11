def solution(progresses, speeds):
    answer = []
    time = 0    # 날짜 수
    count = 0   # 완료된 기능 수
    
    while len(progresses) > 0: # progresses에 항목이 있을 때까지 반복하기
    	# 기능의 진행상황 더하기 지난 날짜만큼의 speed를 곱한걸 더하기
        # 만약 진행상황이 100 이상이면 리스트에서 제거, speed 에서도 제거하고
        # 완료된 기능 수 하나 늘리기
        if(progresses[0]+time*speeds[0])>=100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else: # 기능 진행상황이 100 퍼 이상이 아니면
        	# 만약 완료된 기능이 있다면 answer에 더해준다.
            # 완료된 기능 수는 0으로 초기화한다.
            # 만약 완료된 기능이 없으면 time을 늘린다.
            if count > 0:
                answer.append(count)
                count = 0
            else:
                time+=1
    answer.append(count)
    return answer