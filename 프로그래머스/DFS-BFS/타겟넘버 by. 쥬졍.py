def solution(numbers,target):
    count=0
    
    def dfs(numbers,index,sum,target):
        nonlocal count
        if(index==len(numbers)):
            if(sum==target):
                count+=1
            return 0
        dfs(numbers,index+1,sum+numbers[index],target)
        dfs(numbers,index+1,sum-numbers[index],target)
     
    dfs(numbers,0,0,target)
    
    return count

print(solution([4, 1, 2, 1],4))
            