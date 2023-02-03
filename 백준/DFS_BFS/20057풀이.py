n=int(input())
desert=[list(map(int,input().split())) for _ in range(n)]
now=[n//2,n//2]
left=[(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(-1,0,0.07),(-1,1,0.01),(1,-1,0.1),(1,0,0.07),(1,1,0.01),(0,-2,0.05),(0,-1,0)]
answer=0
right=[(x,-y,z) for x,y,z in left]
down=[(-y,x,z) for x,y,z in left]
up=[(-x,y,z) for x,y,z in down]
rate={'left':left,'right':right,'down':down,'up':up}

def move(cnt,dx,dy,direction):
    global answer
    for _ in range(cnt):
        now[0],now[1]=now[0]+dx,now[1]+dy
        if now[0]<0 or now[1]<0:
            break
        
        spreads=0
        for dx,dy,r in rate[direction]:
            nx,ny=now[0]+dx,now[1]+dy
            if r==0:#알파 부분
                sand=desert[now[0]][now[1]]-spreads
                
            else:
                sand=int(desert[now[0]][now[1]]*r)
                
            if 0<=nx<n and 0<=ny<n:
                desert[nx][ny]+=sand
            else:
                answer+=sand
            spreads+=sand
            
for i in range(1,n+1):
    if i%2!=0:
        move(i,0,-1,'left')
        move(i,1,0,'down')
    
    else:
        move(i,0,1,'right')
        move(i,-1,0,'up')
        
print(answer)
    