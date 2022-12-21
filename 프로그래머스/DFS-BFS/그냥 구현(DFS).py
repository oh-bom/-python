#dfs 구현-재귀 short.ver

graph=[
    [],      # 0
    [2, 3],  # 1 
    [4, 5],  # 2
    [6],     # 3
    [2, 5],  # 4
    [2, 4],  # 5
    [3, 7],  # 6
    [6]
]

visited=[False]*8

def dfs2(v):
    visited[v]=True
    print(v,end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs2(i)


dfs2(1)

#dfs 구현-재귀 long.ver

#참고 사이트: https://heytech.tistory.com/55
def dfs(graph,n,visited):
    visited[n]=True #현재 노드 방문처리
    print(n,end=' ')

    for i in graph[n]:
        if not visited[i]:
            dfs(graph,i,visited)

    
graph=[
    [], # 노드번호가 1부터 시작하기 때문에 인덱스 0은 비워둔다
    [2,3,8], # 1번 노드와 인접한 노드 2,3,8
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]

]

visited=[False]*(8+1)#정점수+1
#dfs(graph,1,visited)