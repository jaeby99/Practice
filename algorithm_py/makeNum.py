from itertools import combinations as cb
def solution(nums):
    answer=0
    for x in cb(nums,3):
        num=sum(x)
        for d in range(2,num):
            if num%d==0:
                break
        else: answer+=1
    return answer
    