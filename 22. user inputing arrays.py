from array import *
arr = array('i',[])
n = int(input("Enter the length : "))
for i in range(n):
    x = int (input("Enter the next value: "))
    arr.append(x)


print(arr)


'''creating 5 element array del 2 array'''
new_arr = array('i',[])
num = int(input("Enter the length: "))
for i in range(num):
    x = int(input("enter the next value: "))
    new_arr.append(x)
d = int(input("enter the value to be deleted: "))

print(new_arr)
new_arr.remove(d)
print(new_arr)

