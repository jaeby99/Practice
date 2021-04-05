def solution(N, stages):
    answer={}
    player=len(stages)
    for x in range(1,N+1):
        if player!=0:
            failure=stages.count(x)
            answer[x]=failure/player
            player-=failure
        else:
            answer[x]=0
    return sorted(answer, key=lambda x: answer[x], reverse=True)