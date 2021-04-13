import math

def solution(progresses, speeds):
    days=[]
    answer=[]
    for x in range(len(speeds)):
        day=math.ceil((100-progresses[x])/speeds[x])
        days.append(day)
    distribute=days[0]
    n=1
    for x in range(1,len(days)):
        if distribute<days[x]:
            answer.append(n)
            distribute=days[x]
            n=1
        else: n+=1
    answer.append(n)
    return answer