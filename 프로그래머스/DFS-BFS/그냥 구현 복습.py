from collections import deque

# def BFS(graph,node,visited):
#     queue=deque([node])
    
#     visited[node]=1
    
#     while queue:
#         q=queue.popleft()
        
#         print(q,end=' ')
        
#         for i in graph[q]:
#             if visited[i]==0:
#                 queue.append(i)
#                 visited[i]=1
            
graph=[
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited=[0]*len(graph)

# BFS(graph,1,visited)


def bfs(graph,node,visited):
    deq=deque([node]) #체크하는 정점들
    print(deq)
    visited[node]=1
    
    while deq:
        q=deq.popleft()
        print(q,end=' ')
        print(deq)
        for i in graph[q]:
            if visited[i]==0:
                deq.append(i)
                visited[i]=1
                
bfs(graph,1,visited)