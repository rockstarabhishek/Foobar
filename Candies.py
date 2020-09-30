for i in range(int(input())):
    n,q  = list(map(int, input().strip().split(" ")))
    array = list(map(int, input().strip().split(" ")))
    sum_list = [0]
    for j in range (q):
        letter , l , r = input().strip().split(" ")
        l = int(l)
        r = int(r)
        su = 0
        if(letter == "U"):
            array[l-1] = r
        elif(letter == "Q"):
            k = 0
            while(l < r+1):
                su = su + (pow(-1,k)*array[l-1]*(k + 1))
                l = l + 1
                k = k + 1
            sum_list.append(su)
    print("Case #{}: {}".format(i+1,sum(sum_list)))