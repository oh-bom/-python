from collections import deque


def solution(field,r,c):
    answer=0
    survived_wolf=0
    survived_sheep=0
    visited=[[0]*c for _ in range(r)]


    def bfs(x,y):
        wolf=0
        sheep=0
    
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        
        deq=deque([(x,y)])
        
        
        while deq:
            x,y=deq.popleft()
            print(x,y,'!')
            visited[x][y]=1
            
            if field[x][y]=='v':wolf+=1
            elif field[x][y]=='o':sheep+=1
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if 0<=nx<r and 0<=ny<c and visited[nx][ny]==0 and field[nx][ny]!='#':
                   
                    deq.append((nx,ny))
        
                    visited[nx][ny]=1
                    
        return wolf,sheep
                    
    
    for i in range(r):
        for j in range(c):
            if field[i][j]!='#' and visited[i][j]==0:
                
                wolf,sheep=bfs(i,j)
                
                print(f'wolf:{wolf} sheep:{sheep}')
                if wolf>=sheep:
                    sheep=0
                else:
                    wolf=0
                    
                    
                survived_wolf+=wolf
                survived_sheep+=sheep
        
        
    print(survived_sheep,survived_wolf)
        

    # deq=deque([0,0,0,0])
        
    # def bfs(i,j,sheep,wolf):
    #     i,j,sheep,wolf=deq.popleft()
        
    #     while deq:
            
    #         if field[i][j]=='v':wolf+=1
    #         if field[i][j]=='o':sheep+=1
            
        
    return answer



r,c=map(int,input().split(' '))
field=[]
for i in range(r):
    field.append(input())
    

solution(field,r,c)