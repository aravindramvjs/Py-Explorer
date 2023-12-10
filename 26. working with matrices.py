from numpy import *
# '''creating a matrix'''

arr = array([
    [1,2,3,4],
    [5,6,7,8]
])
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)
print(arr.size)
'''2d to 1d'''
print(arr.flatten())


'''1d to 2d or more'''
arr1 = array([1,2,3,4,5,6,7,8,9,10,11,12])
arr2= arr1.reshape(6,2)
print(arr2)
arr3 = arr1.reshape(2,2,3)
print(arr3)

'''creating a matix using matrix function matrix function'''
ar =array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])
m = matrix(ar)
print(m)

'''another easy way to write matrix'''
a = matrix('1 2 3 4 ; 5 6 7 8')
print(a)

'''operation in matrix function'''
print(len(a))
print(a.size)
print(a.flatten())
print(a.reshape(2,4))
print(a.min())
print(a.max())
print(a.ndim)


'''adding the matrix'''
a1 = matrix('1 2 3 4 5 ; 6 7 8 9 10')
a2 = matrix('11 12 13 14 15 ; 16 17 18 19 20')
a3 = a1 + a2
print(a3)
