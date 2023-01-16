from collections import deque
import math

def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_sum=0
    deq_truck=deque(truck_weights)
    cnt=0

    while (deq_truck):
        for car in deq_truck:
            if car> math.fllor(weight/2):#혼자 지나가야 하는 차
                    cnt=bridge_length
                    answer.append(cnt)
                    deq_truck.popleft()

            if weight_sum+car>weight:
                break
            
                

           

    return answer