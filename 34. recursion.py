i = 0
def greet():
    global i
    i += 1
    print('Welcome',i)
    greet()

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(100)
greet()





