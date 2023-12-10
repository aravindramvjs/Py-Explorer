# assinging multiple values to a single variable and
# list is mutable
# list is enclosed in [square bracket]

Thisislist = ['this', 'is','list','example']
print(Thisislist)

# to call first value of list

cars = ['Benz','BMW','Audi','Ferrari','Lambogini','ROLLS ROYCE']
print(cars[1])
print(cars[1:3])

# remaming the value example of mutable

cars[0] = 'Volvo'
print(cars)

# combining two lists or nested list

marvel = [['Spiderman'],['Iron man'],['Captain America']]
cars = ['Benz','BMW','Audi','Ferrari','Lambogini','ROLLS ROYCE']
nums = [1,2,3,4,5,6,7]
com = [cars,nums]
print(com)
print(marvel)

# adding value

cars.append('Bugati')
print(cars)

# inserting values

cars.insert(1,'TaTa Air')
print(cars)

# removing values

cars.remove('Benz')
print(cars)

# poping values

cars.pop(0)
print(cars)

# if u use pop() without any index value it will pop last value

cars.pop()
print(cars)

# ctrl + space for more option