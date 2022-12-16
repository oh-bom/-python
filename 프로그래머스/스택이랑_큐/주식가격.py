from collections import deque

def solution2(prices):
    answer = []
    deq_prices=deque(prices)
    dis=0
    while (deq_prices):
        x=deq_prices.popleft()
        
        for y in deq_prices:
            
            if x>y :#멈출타이밍
                dis+=1
                break

            else:# 그렇지 않은 경우엔 거리 +1
                dis+=1

            #사실 위의 코드들 더 간단히 하면
            # dis+=1
            # if x>y: break
        
        answer.append(dis)
        dis=0

    return answer

print(solution2([1,2,3,2,3]))

#index로 풀려던,,
def solution(prices):
    answer = []
    deq=deque(prices)


    for i in range(0,len(prices)-1):
        dis=0
        for j in range(i+1,len(prices)):
            dis+=1
            if prices[j]<prices[i]:#멈추자
                break
              
        answer.append(dis)

    answer.append(0)
    return answer

print(solution([1,2,3,2,3]))