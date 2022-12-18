from collections import deque

def solution(s):
    
    deq_str=deque(s)
    storage=deque()
    answer = True

    while (deq_str):
        x=deq_str.popleft()
        if x=='(':storage.append(x)
        else:
            if not storage: 
                answer=False
                break
            value=storage.pop()
            if value!='(':
                answer=False
                break

    if storage: answer=False

    return answer



print(solution(")()("))