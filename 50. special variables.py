# the __name__ is a special variables and tells the compiler to starting point
from demo import *
def sum(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def main():
    sum(1,2)
    sub(5,4)


if __name__=="__main__":
    main()
