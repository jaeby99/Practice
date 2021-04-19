def solution(prices):
    time=[0]*len(prices)
    for x in range(len(prices)-1):
        pr1=prices[x]
        for y in range(x+1, len(prices)):
            time[x]+=1
            if pr1>prices[y]: break
    return time