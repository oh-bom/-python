
def solution(r,c,field):
    answer=0
    visited=[[0]*c for _ in range(r)]
    survived_wolf=0
    survivied_sheep=0
    
    
    def dfs(x,y):
        visited[x][y]=1
        
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        
        global wolf,sheep
        
        if field[x][y]=='v':wolf+=1
        elif field[x][y]=='o':sheep+=1
        
        #print(f'wolf:{wolf}, sheep:{sheep}')
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
      
            if 0<=nx<=r-1 and 0 <=ny<=c-1 and visited[nx][ny]==0 and field[nx][ny]!='#':dfs(nx,ny)
            
            
    for i in range(r):
        for j in range(c):
            if field[i][j]!='#' and visited[i][j]==0:
                global wolf,sheep
                wolf=0
                sheep=0
                
                dfs(i,j)
                
                if wolf>=sheep:
                    sheep=0
                else:
                    wolf=0
                    
                survived_wolf+=wolf
                survivied_sheep+=sheep
    
    print(survivied_sheep,survived_wolf)
    return


r,c=map(int,input().split(" "))

field=[]

for _ in range(r):
    field.append(input())

print(solution(r,c,field))
