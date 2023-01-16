import math

def solution(numbers):
    answer=0
    for n in numbers:
        num_list=[]
        num_list.append(int(n))

    i=0
    def dfs(num,i):
        nonlocal answer
        cnt=0
        for i in range(2,math.sqrt(num)):
            if num%i ==0: cnt+=1 #소수가 아닌 경우

        if cnt==0:
            answer+=1
        
        dfs()



    answer = 0
    return answer