def solution(priorities, location):
    answer = 0
    # 시작 기준이 되는 중요도가 가장 큰 프로세스의 인덱스를 저장해놓기
    standard = priorities.index(max(priorities))
    
    # 원하는 답을 구할 때까지 반복하도록 작성한다.
    while True:
        # 중요도가 가장 큰 프로세스의 값을 저장해놓기
        value = max(priorities)
        
        # 만약 중요도가 가장 큰 프로세스의 값과 기준 인덱스의 value 값이 같다면
        # 프로세스가 실행되므로 중요도 값을 0으로 저장하고 실행 수를 1 늘린다.
        if priorities[standard] == value:
            priorities[standard] = 0
            answer += 1
            
            # 만약에 기준 인덱스와 실행순서를 찾고싶은 인덱스(location) 이 같다면
            # 반복문을 탈출한다.
            if standard == location:
                break
                
        # 프로세스가 실행이 안되어도 다음 프로세스의 비교를 위해 다음으로 넘어간다.
        standard += 1
        # 만약 프로세스 순서가 priorities 리스트의 끝 순서까지 간다면 첫번째(0) 으로 옮긴다.
        if standard == len(priorities):
            standard = 0
    return answer