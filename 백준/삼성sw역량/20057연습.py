n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]

left=[(-1,1,0.01),(1,1,0.01),(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(1,-1,0.1),(0,-2,0.05),(0,-1,0)]
right=[(x,-y,z) for x,y,z in left]
down=[(-y,x,z) for x,y,z in left]
up=[(-x,y,z) for x,y,z in down]
now=[n//2,n//2]
outside_sand=0

direction={'left':left,'right':right,'down':down,'up':up}

def move(index,dx,dy,dir):
    global outside_sand
    
    for _ in range(index):
        now[0],now[1]=now[0]+dx,now[1]+dy
        
        if now[0]<0 or now[1]<0:break
        
        #뿌려지는 모래들
        spreads=0
            
        for x,y,r in direction[dir]:
            nx=now[0]+x
            ny=now[1]+y
            if r==0:
                sand=board[now[0]][now[1]]-spreads
            else:
                sand=int(board[now[0]][now[1]]*r)
            
            if 0<=nx<n and 0<=ny<n:
                board[nx][ny]+=sand
                
            else:
                outside_sand+=sand
                
            spreads+=sand
     

for i in range(1,n+1):
    if i%2!=0:
        move(i,0,-1,'left')
        move(i,1,0,'down')
    else:
        move(i,0,1,'right')
        move(i,-1,0,'up')
print(outside_sand)