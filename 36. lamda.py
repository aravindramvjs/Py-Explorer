'''function to even number'''
def square(a):
    return a*a


result = square(2)
print(result)

'''instead of defing a function 
we can lamda function to write code in single line'''

f = lambda a:a*a
res = f(3)
print(res)

b = lambda p,q:p+q #for addtion
show = b(2,4)
print(show)
