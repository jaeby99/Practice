from itertools import combinations as c

def solution(phone_book):

    sortedPB=sorted(phone_book)
    for a, b in c(sortedPB, 2):
        if a==b[:len(a)]:
            return False
    return True