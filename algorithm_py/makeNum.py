def solution(nums):
    num_sum=[]
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            for z in range(y+1, len(nums)):
                    num_sum.append(nums[x]+nums[y]+nums[z])
    answer=len(num_sum)
    for x in range(len(num_sum)):
        for d in range(2,num_sum[x]):
            if num_sum[x]%d==0:
                answer-=1
                break
    return answer