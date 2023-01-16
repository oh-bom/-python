from collections import deque

def solution(maps):
    
    m=len(maps)
    n=len(maps[0])
    
    def bfs(i,j):
        queue=deque()
        queue.append((i,j,0))
        
        while queue:
            
           
            i,j,distance=queue.popleft()
            distance+=1
            
            # if i<0 or i>= m or j<0 or j>= n:return 0
            if i==n-1 and j==m-1: return distance
            
            if maps[i][j]==0: continue
            
            maps[i][j]=0
            
        
            print(i,j,distance)
            if i<n-1:
                queue.append((i+1,j,distance))
            if j<m-1:
               queue.append((i,j+1,distance))
            if i>0:
               queue.append((i-1,j,distance))
            if j>0:
                queue.append((i,j-1,distance))
                
    return bfs(0,0)

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
