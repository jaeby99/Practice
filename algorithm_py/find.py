def solution(n):
    num=set(range(2,n+1))
    for x in range(2,n+1):
        if x in num:
            num-=set(range(2*x,n+1,x))
    return len(num)