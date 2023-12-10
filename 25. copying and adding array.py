from numpy import *


'''adding num to each array'''
print('adding num to each array')
arr = array([1,2,3,4,5,6,7])
arr+=5
print(arr)



'''adding two arrays also called as vectorized operation'''
print('adding two arrays')
arr1 = array([11,12,13,14,15])
arr2 = array([16,17,18,19,20])
arr3 = arr1+arr2
print(arr3)

'''operations on array'''
print('operations on array')
print(log(arr))
print(sin(arr))
print(tan(arr))
print(cos(arr))
print(min(arr))
print(max(arr))
print(sqrt(arr))
print(sort(arr))
print(concatenate([arr1,arr2]))


'''copying arrays'''
'''aliasing which copies array but are in same memory'''
print('aliasing array')
a1 = array([10,11,1,31,4,5])
a2 = a1
print(a1,a2)
print(id(a1),id(a2))



'''shallow copy which are in different memory but depend each other, 
if one value change all value will change'''

print('shallow copy')
arra1 = array([1,2,3,4,5,6])
arra2 = arra1.view()
print(arra1,id(arra1))
print(arra2,id(arra2))
arra2[2]=5
print(arra1)
print(arra2)


'''deep copy means simply copying array 
which does't change original value'''

print('deep copy')
r1 = array([1132,1232,314,13,34,12])
r2 = r1.copy()
print(r1,id(r1))
print(r2,id(r2))
r2[2]=5
print(r1)
print(r2)


