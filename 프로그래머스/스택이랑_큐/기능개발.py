from collections import deque
import math

#다른풀이 보고 수정한 코드(by. RohTaeHyeon님)
def solution2(progresses, speeds):
    answer = []

    deq_period=deque([])
    for i in range(0,len(progresses)):
        need_rate=100-progresses[i]
        need_day=math.ceil(need_rate/speeds[i])
        deq_period.append(need_day)
    
    cnt=1
    while (deq_period):
        if cnt>1:
            deq_period.popleft()
            cnt-=1
            continue

        x=deq_period.popleft()
        for p in deq_period:
            if x>=p:
                cnt+=1
            else:
                break

        answer.append(cnt)
       
    return answer

#나의 조금 망한 코드(미완)
def solution(progresses, speeds):
    answer = []

    deq_period=deque([])
    for i in range(0,len(progresses)):
        need_rate=100-progresses[i]
        need_day=math.ceil(need_rate/speeds[i])
        deq_period.append(need_day)
    
    count=1
    j=0
    while True:
        if len(deq_period)==0: break
        for i in range(0,len(deq_period)):
            print(i,len(deq_period))
            if len(deq_period)==1:
                answer.append(1)
                deq_period.popleft()
                break
               

            if deq_period[i]>deq_period[i+1]:
                count+=1
                deq_period.popleft()
                
                
            else:
                answer.append(count)
                deq_period.popleft() 
                break
                
        

    return answer



print(solution2([93, 30, 55],[1,30,5]))
print(solution2([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
