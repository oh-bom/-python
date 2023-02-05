r,c=map(int,input().split())

#board=[list(input()) for _ in range(r)]

board=[]
for _ in range(r):
    board.append(list(input()))
def solution(r,c,board):
    cmp=[]
    for a in range(r-7):
        for b in range(c-7):
            w_cnt=0
            b_cnt=0
            for i in range(a,a+8):
                for j in range(b,b+8):
                    if (i+j)%2==0:
                        if board[i][j]=='B':w_cnt+=1
                        else: b_cnt+=1
                    else:
                        if board[i][j]=='B':b_cnt+=1
                        else:w_cnt+=1
                        

            cmp.append(w_cnt)
            cmp.append(b_cnt)
    
    print(min(cmp))
    

solution(r,c,board)
    