def solution(s):
    d=0
    answer=""
    words=list(s)
    for x in range(len(words)):
        w="".join(words[x])
        if words[x]==" ":
            d=0
        elif d==0:
            w=w.upper()
            d=1
        elif d==1:
            w=w.lower()
            d=0
        answer+=w
    return answer