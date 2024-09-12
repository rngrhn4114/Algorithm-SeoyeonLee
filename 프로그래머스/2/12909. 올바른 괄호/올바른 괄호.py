def solution(s):
    answer = True
    stack = []
    
    #문자열 s 순회
    for i in s:
        # 만약 i 가 ( 이면, stack에 추가한다.
        if i == '(':
            stack.append(i)
        else: # 만약 i 가 ) 이면, 
            if stack == []:   # 그때 stack 이 비어있으면 )로 시작하므로 False return
                return False
            else: # 만약 stack에 비어있지 않으면 (를 삭제해준다.
                stack.pop()
    if stack != []: 
        # 만약 순회를 다 돌았는데 stack이 비어있지 않다면('(' 가 남아있다면)False return
        return False
    return answer