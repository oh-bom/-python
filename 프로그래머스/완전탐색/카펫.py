import math

#다른 풀이,,허허다들 정말 똑디하시다,,
def solution2(brown,red):
    s=brown+red
    for n in range(1,s+1):
        if s%n!=0:
            continue
        m=s/n
        if (n-2)(m-2)==red:
            return sorted([n,m],reverse=True)

#내 풀이(문제 제대로 안봐서 뻘짓,,^__^)
def solution(brown, yellow):
    answer = []

    b_row=0
    b_col=0
    
    cycle=int(math.ceil((brown+yellow)/2))

    for i in range(1,cycle):    
        for y_col in range(1,yellow+1):
            if yellow%y_col==0:
                y_row=int(yellow/y_col)
               
            b_row=y_row+i*2
            b_col=y_col+i*2
            print(b_row,b_col)
            if b_row*b_col>brown+yellow:
                continue

            if b_row* b_col== brown+yellow:
                answer.append(b_row)
                answer.append(b_col)
                return answer
        




print(solution(8,1))