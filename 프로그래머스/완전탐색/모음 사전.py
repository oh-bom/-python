import math

def solution(word):
    word=list(word)
    d={"A":1,'E':2,'I':3,'O':4,'U':5}
    answer=0
    sum=0

    c=1 #몇번째로 나오는 수인지
    for x in word:
        
        a=d[x]-d['A']

        for i in range(0,5-c+1):
            sum+=math.pow(5,i)
            print(a,sum)
      
        answer+=(sum*a)
        c+=1
    return answer

print(solution("EIO"))