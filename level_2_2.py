import math
def solution(total_lambs):
    if total_lambs >= 10**9:
        return 0
    doubledList=[]
    x=0
    runningtotal=0
    while x<= total_lambs:
        currentvalue=2**x
        doubledList.append(currentvalue)
        runningtotal=runningtotal + currentvalue
        if runningtotal > total_lambs:
            break
        x=x+1
    fiblist=[1,1]
    fibrunningtotal=2
    y=2
    while y<= total_lambs:
        value=fiblist[y-1] + fiblist[y-2]
        fiblist.append(value)
        fibrunningtotal=fibrunningtotal + int(fiblist[y])
        if fibrunningtotal > total_lambs:
            break
        y=y+1
    solution = len(fiblist) - len(doubledList)
    return abs(solution)
def solution1(total_lambs):
    min_n = int(math.log2(total_lambs + 1))
    max_n = 1
    a = 0
    b = 1
    total = 1
    while(1):
        c = a + b
        total += c
        #print("max_n = ",max_n , "total = " ,total)
        if total > total_lambs :
            break
        else:
            max_n += 1
            a = b
            b = c
    return  (max_n - min_n)
for i in range(10000,1000000):
    if(solution(i) > solution1(i)):
        print(i,'less by ', solution(i) - solution1(i) )
    elif(solution(i) < solution1(i)):
        print(i,'less by ', solution1(i) - solution(i) )