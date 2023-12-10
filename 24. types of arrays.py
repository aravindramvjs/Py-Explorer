'''LINSPACE MEANS DIVIDES THE RANGE INTO PARTS '''
from numpy import *
arr =linspace(1,10,11)
print(arr)
arr =linspace(1,10,2)
print(arr)



'''LOGSPACE MEANS DIVIDES THE RANGE AND 
THE SPACING BETWEEN TWO ELEMENT WOULD LOG OF IT'''
arr =logspace(1,10,5)
print(arr)



'''arange means skip the specific number'''
arr = arange(1,50,3)
print(arr)


'''ZEROS ARE GIVES NO OF zeros SPECIFY'''
arr = zeros(5)
print(arr)


'''ones gives no of ones specify'''
arr = ones(5)
print(arr)
arr = ones(5,int)
print(arr)