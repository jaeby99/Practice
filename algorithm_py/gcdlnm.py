def solution(a,b):
    m,n=max(a,b), min(a,b)
    t=1
    while t>0:
        t=m%n
        m,n=n,t
    return [m, int(a*b/m)]