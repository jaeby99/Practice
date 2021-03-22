def solution(x):
    num=x
    div=0
    for i in range(len(str(x))-1,-1,-1):
        div=div+int(num/10**i)
        num=num%10**i
    return x%div==0