def solution(progresses, speeds):
    d=[]
    for p,s in zip(progresses, speeds):
        if len(d)==0 or d[-1][0] < -((p-100)//s):
            d.append([-((p-100)//s),1])
        else:
            d[-1][1]+=1
    return [x[1] for x in d]