import math
def solution(num,board):
    sand_outside_amount=0
    
    def sand_change_col(x,y):
        dx=[-1,1,-1,1,-2,2,-1,1,0]
        dy=[1,1,0,0,0,0,-1,-1,-2]
        ratio=[1,1,7,7,2,2,10,10,5]
        n=len(dx) #9
        nonlocal sand_outside_amount
        
        for i in range(n):
            nx=x+dx[i]
            ny=y+dy[i]
            
            
            sand=math.trunc(board[x][y]*ratio[i]*0.01)
            if (0<=nx<num) and (0<=ny<num):
                board[nx][ny]+=sand
                #print(f'success:{nx},{ny}')
            else:
                sand_outside_amount+=sand
                print(f'not success:{nx},{ny} {sand_outside_amount}')
                
        
        alpha=math.trunc(board[x][y]*55*0.01)
        if (0<=x<num) and (0<=y-1<num): board[x][y-1]+=alpha
        else: sand_outside_amount+=alpha
       
        
    def sand_change_row(x,y):
        
        dx=[0,0,-1,1,2,-1,0,1,0]
        dy=[-2,-1,-1,-1,0,1,1,1,2]
        ratio=[2,7,1,10,5,1,7,10,2]
        nonlocal sand_outside_amount
        n=len(dx) #9
        
        for i in range(n):
            nx=x+dx[i]
            ny=y+dy[i]
            
            sand=math.trunc(board[x][y]*ratio[i]*0.01)
            if (0<=nx<num) and (0<=ny<num):
                board[nx][ny]+=sand
                #print(f'success:{nx},{ny}')
            else:
                #print(f'not success:{nx},{ny} {sand_outside_amount}')
                sand_outside_amount+=sand
        
        #print(x,y)
        alpha=math.trunc(board[x][y]*55*0.01)
        if (0<=x+1<num) and (0<=y<num): board[x+1][y]+=alpha
        else: sand_outside_amount+=alpha
        
        
                
            
            
    def tonado(x,y,num):
        odd_dx=1
        odd_dy=-1
        even_dx=-1
        even_dy=1
        for i in range(1,num):
            if i%2 !=0:
                for _ in range(i):
                    y+=odd_dy
                    print(f'!{x} {y}')
                    if board[x][y]!=0:
                        sand_change_col(x,y)
                for _ in range(i):
                    x+=odd_dx
                    print(f'!{x} {y}')
                   
                    if board[x][y]!=0:
                        sand_change_row(x,y)
            else:
                for _ in range(i):
                    y+=even_dy
                    print(f'!{x} {y}')
                    if board[x][y]!=0:
                        sand_change_col(x,y)
                for _ in range(i):
                    x+=even_dx
                    print(f'!{x} {y}')
                    if board[x][y]!=0:
                        sand_change_row(x,y)
                
        #맨 마지막 변 한번더
        if i==num-1:
            for _ in range(i):
                y=-1
                if board[x][y]!=0:
                    sand_change_col(x,y)
                    
    center=num//2
    tonado(center,center,num)
    return sand_outside_amount
        
        
            
    
    
num=int(input())
board=[]
for _ in range(num):
    board.append(list(map(int,input().split())))
print(board)
print(solution(num,board))