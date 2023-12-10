def fact(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
        print(a)
    return a    #return is used to goto 'a' again after multipling


result = fact(5)
