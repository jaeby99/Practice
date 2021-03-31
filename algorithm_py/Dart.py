import re

def solution(dartResult):
    bonus={'S':1, 'D':2, 'T':3}
    option={'':1, '*':2, '#':-1}
    dart=re.compile('(\d+)([SDT])([#*]?)')
    score=dart.findall(dartResult)
    for x in range(len(score)):
        if score[x][2]=='*' and x>0: 
            score[x-1]*=2
        score[x]=int(score[x][0])**bonus[score[x][1]]*option[score[x][2]]
        
    answer=sum(score)
    return answer