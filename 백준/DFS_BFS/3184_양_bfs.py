from collections import deque

def solution(field,n,m):
    answer=0


    deq=deque([0,0,0,0])
        
    def bfs(i,j,sheep,wolf):
        i,j,sheep,wolf=deq.popleft()
        
        while deq:
            
            if field[i][j]=='v':wolf+=1
            if field[i][j]=='o':sheep+=1
            
        
    return answer




n,m=map(int,input().split(' '))
field=[]
for i in range(n):
    field.append(input())
    
print(field)
solution(field,n,m)