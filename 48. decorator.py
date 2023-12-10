def div(a,b):    #the pre existing function which cant access for us
    print(a/b)


def smartdiv(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smartdiv(div)             #indirect calling fuction
div(2,4)