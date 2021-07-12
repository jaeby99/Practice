from collections import deque

def solution(priorities, location):
    count=0
    length=len(priorities)
    enum_prior=deque(enumerate(priorities))
    p=max(priorities)
    
    while len(enum_prior)!=0:
        if enum_prior[0][1]!=p:
            key=enum_prior[0]
            enum_prior.popleft()
            enum_prior.append(key)
        else:
            count+=1
            if enum_prior[0][0]==location:
                return count
            else:
                priorities.remove(p)
                enum_prior.popleft()
                p=max(priorities)
    return length