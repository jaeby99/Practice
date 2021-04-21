def solution(bridge_length, weight, truck_weights):
    time=0
    que=[0]*bridge_length
    
    for x in truck_weights:
        sum_weight=sum(que)+x
        if sum_weight<= weight:
            que.pop(0)
            que.append(x)
            time+=1
        elif sum_weight>weight:
            count=0
            while sum(que)>weight-x:
                count+=1
                que.pop(0)
            for i in range(count-1):
                que.append(0)
            que.append(x)
            time+=count
            
    while len(que)!=0:
        que.pop(0)
        time+=1
        
    return time