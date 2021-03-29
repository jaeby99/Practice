def solution(n, arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        st=""
        for x in range(n-1,-1,-1):
            num=2**x
            if arr1[i]>=num or arr2[i]>=num:
                st+='#'
                arr1[i]%=num
                arr2[i]%=num
            else:
                st+=" "
        answer.append(st)
    return answer