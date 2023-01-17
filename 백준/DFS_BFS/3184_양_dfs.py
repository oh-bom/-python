import sys

def solution():
    input=sys.stdin.readline

    r,c=map(int,input().split())

    board=[]
    visited=[[0]*c for _ in range(r)]

    for _ in range(r):
        board.append(list(input().rstrip()))
        
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
        
    def dfs(x,y):
        global w,s

        visited[x][y]=1
        
        if board[x][y]=='v':
            w+=1
        elif board[x][y]=='o':
            s+=1
            
        print(f'wolf:{w}, sheep:{s}')
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<r and 0<=ny<c and board[nx][ny]!="#" and visited[nx][ny]==0:
                dfs(nx,ny)
                
    wolf=0
    sheep=0

    for i in range(r):
        for j in range(c):
            if board[i][j]!="#" and visited[i][j]==0:
                global w,s
                w=0
                s=0
                dfs(i,j)
                
                if w>=s:
                    s=0
                    
                else:
                    w=0
                    
                wolf+=w
                sheep+=s
    print(sheep,wolf)
    
solution()
             