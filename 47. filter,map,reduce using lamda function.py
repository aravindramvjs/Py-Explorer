'''filter fun filters the given data'''


nums = (1,2,3,4,5,6,7,8,9,10)
evens = list(filter(lambda a:a%2==0,nums))
print(evens)
three_multi = list(filter(lambda a:a%3==0,nums))
print(three_multi)

'''map func map the value'''

add_all = list(map(lambda n : n+2,evens))
print(add_all)

'''reduce func will add all values and gives one value'''
'''to use we need to import the module functiontool'''
from functools import reduce
sum = reduce(lambda a,b:a+b,nums)
print(sum)