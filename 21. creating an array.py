'''creating an array'''

from array import *
vals = array('i',[1,2,3,4,5])
print(vals)

'''methods of array'''
print(vals.buffer_info())
vals.append(6)
print(vals)
print(vals.typecode)
print(vals.itemsize)
vals.reverse()
print(vals)

'''iterating arrays if range is unknown'''
for e in range(len(vals)):
    print(e)

'''if type is unknown'''
print('new array')
new_arr = array(vals.typecode,(a for a in vals ))
print(new_arr)
