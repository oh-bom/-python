##내가 푼 코드
def solution(people, limit):
    answer = 0
    ck=[]
    for i in range(len(people)):
        ck.append(0)
    sum=0
    for i in range(0,len(people)):
        for j in range(i+1,len(people)):
            sum=people[i]+people[j]
            if(sum<=limit and ck[i]==0 and ck[j]==0):
                answer+=1
                ck[i]=1
                ck[j]=1
        if(ck[i]==0):
            answer+=1
    return answer

x=solution([70, 50, 80, 50],100)
print(x)

##deque이용한 풀이 코드 !!(by. uos2016님)
from collections import deque

def solution2(people,limit):
    answer=0
    deq=deque(sorted(people))
    while deq:
        if len(deq)==1:##더이상 데큐에 남은 원소가 없어 마지막 사람이 혼자 보트타는 경우
            answer+=1
            break
        if deq[0]+deq[-1]<=limit: ##둘이 함께 보트 탈 수 있는 경우
            deq.pop()
            deq.popleft()
        else: ##혼자서 보트 타는 경우
            deq.pop()

        answer+=1

    return answer

print(solution2([70,50,40,80],100))