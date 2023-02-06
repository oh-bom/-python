from collections import deque

def solution(life,dungeons):
    n=len(dungeons)
    answer=[]
    
    def dfs(cnt,life,index):
        least_piro,consume_piro=dungeons[index]
        
        if visited[index]==0 and life>=least_piro:
            visited[index]=1
            cnt+=1
            life-=consume_piro
            
        for i in range(n):
            if visited[i]==0:
                dfs(cnt,life,i)
        
        return cnt
    
    for i in range(n):
        
        answer.append(dfs(0,life,i))
        
        
    return max(answer)
            
                
dungeons=[[80,20],[50,40],[30,10]]
#visited=[[0]*len(dungeons)]
visited=[0 for _ in range(len(dungeons))]


solution(80,dungeons)
    
    