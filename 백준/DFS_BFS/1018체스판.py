import sys
def solution(r,c,board):
    
    def dfs(x,y,board2):
        count=0
        board3=list(board2)
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if board3[x][y]=='W':
                if 0<=nx<r and 0<=ny<c and board3[nx][ny]=='W':
                    count+=1
                    board3[nx][ny]='B'
            else:
                if 0<=nx<r and 0<=ny<c and board3[nx][ny]=='B':
                    count+=1
                    board3[nx][ny]='W'
        return count
    
    dr=r-8+1
    dy=c-8+1
    
    min=sys.maxsize
    
    print(f'dr:{dr} dy:{dy}')
    for x in range(0,dr):
        for y in range(0,dy):
            print("~~")
            print(x,y)
            print("~~")
            sum=0
            board2=list(board)
            print(board2)
            print(f'first sum:{sum}')
            for i in range(x,x+8):
                for j in range(y,y+8):
                    #print(i,j)
                    cnt=dfs(i,j,board2)
                    #print(f'cnt:{cnt}')
                    sum+=cnt
            print(f'sum:{sum}')
            
            if sum<min:min=sum
        
    return min
            
    
    

#input=sys.stdin.read()
r,c=map(int,input().split())
board=[]
board2=[]
for _ in range(r):
    board.append(list(input()))
    
solution(r,c,board)