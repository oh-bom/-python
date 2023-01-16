def solution(maps):
    answer=0
    
    n=len(maps)
    m=len(maps[0])
    
    def dfs(i,j,distance):
        maps[i][j]=0
        
        print(i,j,distance)
        
        if i==n-1 and j==m-1:
            print("?")
            print(distance)
            return distance
        
        
        if i<n-1 and maps[i+1][j]==1: dfs(i+1,j,distance+1)
        if j<m-1 and maps[i][j+1]==1: dfs(i,j+1,distance+1)
        if i>0 and maps[i-1][j]==1: dfs(i-1,j,distance+1)
        if j>0 and maps[i][j-1]==1: dfs(i,j-1,distance+1)
        
        
    return dfs(0,0,1)

maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(f'answer:{solution(maps)}')