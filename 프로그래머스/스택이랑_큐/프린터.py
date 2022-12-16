from collections import deque

#deque와 max 사용 (by.RohTaeHyeon님)
def solution(priorities, location):
    deq=deque(priorities)
    my_doc=[0 for _ in range(len(priorities))]
    my_doc[location]=1
    my_doc=deque(my_doc)
    cnt=0
    answer = 0
    
    while(my_doc):
        priority=deq.popleft()
        check_my_doc=my_doc.popleft()

        if len(deq)>1 and max(deq)>priority:
            deq.append(priority)
            my_doc.append(check_my_doc)

        else:
            cnt+=1
            if check_my_doc==1:
                answer=cnt
                break
    return answer

#안보고 연습
def solution2(priorities, location):
    answer = 0
    cnt=0
    deq=deque(priorities)
    my_doc=[0 for _ in range(len(priorities))]
    my_doc[location]=1
    my_doc=deque(my_doc)

    while (my_doc):
        now_pri=deq.popleft()
        now_doc=my_doc.popleft()

        if len(deq)>1 and now_pri<max(deq):
            deq.append(now_pri)
            my_doc.append(now_doc)

        else:
            cnt+=1
            if now_doc==1:
                answer=cnt
                break
    return answer
    

print(solution2([3,4,1,0],0))