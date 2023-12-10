'''at default it is string when we spicify int it becomes integer datatype'''
x = int(input("Enter the value of X: ") )
y = int(input("Enter the value of Y: "))
print("The output is", x+y)

'''geting a single char from the user'''
yorn = input("Enter Y or N: ")[0] #[0] for geting only first char
print(yorn)

'''eval func will do math operation '''
robot = eval(input("solve a math func:"))
print(robot)