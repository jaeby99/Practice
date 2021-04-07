def solution(clothes):
    hash_map={}
    keys=[]
    answer=1
    for x in clothes:
        if x[1] not in hash_map:
            hash_map[x[1]]=1
            keys.append(x[1])
        else:
            hash_map[x[1]]+=1
    
    for cloth in keys:
        answer*=(hash_map[cloth]+1)
        
    return answer-1