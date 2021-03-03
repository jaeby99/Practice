def solution(s, n):
    s=list(s)
    for x in range(len(s)):
        if s[x].isupper():
            s[x]=chr((ord(s[x])-ord('A')+n)%26+ord('A'))
        elif s[x].islower():
            s[x]=chr((ord(s[x])-ord('a')+n)%26+ord('a'))
    return "".join(s)