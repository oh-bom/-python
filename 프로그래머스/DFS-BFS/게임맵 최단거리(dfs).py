
from collections import deque

def solution(maps):
    cnt=0
    def dfs(x,y):
        nonlocal cnt
        visited[x][y]=1
        cnt+=1
        if x<=-1 or x>= n+1 or y<= -1 or y>= m+1:#영역밖의 범위
            return -1
            
        if x==(n-1) and y==(m-1): #목적지 도달
            print(x,y,cnt)
            visited[x][y]=1
            return cnt
    
        print(x,y)

        if(visited[x+1][y]==0 and graph[x+1][y]==1):
            dfs(x+1,y)
          
        if(visited[x][y+1]==0 and graph[x][y+1]==1):
            dfs(x,y+1)
            
        if(visited[x-1][y]==0 and graph[x-1][y]==1):
            dfs(x-1,y)
            
        if(visited[x][y-1]==0 and graph[x][y-1]==1):
            dfs(x,y-1)

        #cnt-=1
        #visited[x][y]=0
        return 0
    
    graph=[]
    n=len(list(maps[0]))
    m=len(maps)
  
    visited=[[0]*(n) for _ in range(m)]
    visited2=[[0]*(n) for _ in range(m)]
    
    for i in range(m):
            graph.append(maps[i])

    answer=0
    #for i in range(n):
     #   for j in range(m):
      #      if(dfs(i,j)>0):
       #         print(dfs(i,j))

    #dis=dfs(0,0)
    x=dfs(0,0)
    print(x)

    #return max(answer)
    return 100
maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
solution(maps)