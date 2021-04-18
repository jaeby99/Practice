def solution(priorities, location):
    sorted_priorities=sorted(priorities, reverse=True)
    count=0
    pos=0
    for x in sorted_priorities:
        for n in range(len(priorities)):
            if pos>=len(priorities): pos=0
            if x==priorities[pos]:
                count+=1
                if pos==location: return count
                else: pos+=1
                break
            else: pos+=1
        if pos>=len(priorities): pos=0