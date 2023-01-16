def solution(numbers, target):
    cnt=0
    
    def dfs(i,sign,target):
        nonlocal cnt
        
        if i==len(numbers):
            if sum==target:
                cnt+=1
            return
        
        sum+=numbers[i]*sign
        
        dfs(i+1,1,sum)
        dfs(i+1,-1,sum)
        
    for sign in [-1,1]:
        dfs(0,sign,0)
        
    return int(cnt/2)
    