from collections import deque

def solution(n, computers):
    answer = 0
    
    graph=[[0]*(2) for _ in range(n)]
    visited=[0]*n
    print(graph)


    for list in computers:
        for i in range(n):
            for j in range(i+1,n):
                print(i,j)
                if list[i]==list[j]==1:
                    print("!")
                    graph[i][j]=1
                    graph[j][i]=1

    def bfs(v):
        q=deque()
        q.append(v)
        visited[v]=1

        while q:
            v=q.popleft()
            for i in graph[v]:
                if visited[v+1]==0 and graph[v][v+1]==1:
                    visited[v+1]=1
                    q.append(v)
                    return True

        return False

    for i in range(n):
        if bfs(i)==True:
            answer+=1


    return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])

