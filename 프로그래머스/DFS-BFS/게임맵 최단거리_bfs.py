#다른 풀이 참고(by. w00cheol님)

from collections import deque

def solution(maps):
    m=len(list(maps[0]))
    n=len(maps)
    
    def bfs(x,y):
        q=deque()
        q.append((x,y,1))

       
        while q:
            x,y,distance=q.popleft()

            print(x,y,distance)
            if x==n-1 and y==m-1:
                return distance
            if maps[x][y]==0:#막혀서 못가는 부분
                continue
            maps[x][y]=0 #이제 방문한거니까 못가게 0으로 바꾸기

            if x+1 < n:
                q.append((x+1, y, distance+1))
            if y+1 < m:
                q.append((x, y+1, distance+1))
            if y-1 >= 0:
                q.append((x, y-1, distance+1))
            if x-1 >= 0:
                q.append((x-1, y, distance+1))

        return -1
    return bfs(0,0)

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))

    