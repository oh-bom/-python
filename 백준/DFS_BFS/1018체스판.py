import sys

#내가 해봤던 코드,,
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
            
            
#풀이
def solution2(r,c,board):
    compare=[]
    for a in range(r-7):
        for b in range(c-7):
            w_index=0
            b_index=0
            
            for i in range(a,a+8):
                for j in range(b,b+8):
                    if (i+j)%2==0:#시작하는 색이 나와야하는 칸
                        if board[i][j]=='B':
                            w_index+=1
                        else:b_index+=1
                        
                    else:
                        if board[i][j]=='B':
                            b_index+=1
                        else:w_index+=1
            
            compare.append(w_index)
            compare.append(b_index)
            
    return min(compare)
            
#input=sys.stdin.read()
r,c=map(int,input().split())
board=[]
board2=[]
for _ in range(r):
    board.append(list(input()))
    
#solution(r,c,board)
print(board)
print(solution2(r,c,board))