# swaping two variables with constant variable

print("with third variable")

a = 5
b = 10
print(a,b)

temp = a #constant variable
a = b
b = temp

print(a,b)

print("without third variable")
print("method 1")
print(a,b)
a = a+b #5+10 = 15
b = a-b #15-10 = 5
a = a-b #15-5 = 10
print(a,b)

print("method 2 with xor ")
# this memory efficient
a = a^b
b = a^b
a = a^b

print("easy method")
a,b = 5,6
print(a,b)
b,a = 5,6 # it just rotate the value
print(a,b)