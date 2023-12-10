#constructor is used to construct an object
#__init__ is constuctor here
#self is used to assing and access the values

class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def confriguation(self):
        print("The confriguation for computer is",self.cpu,self.ram)
 
com1 = computer('i5',12)
com2 = computer('i3',16)

com1.confriguation()
com2.confriguation()

class cycle:
    def __init__(owner,body,wheel,bell,seat):
        owner.stand = body
        owner.under = wheel
        owner.center = seat
        owner.handbar = bell

    def work(owner):
        print('The cycle is constructed by ',owner.stand,owner.under,owner.center,owner.handbar)

hercules =cycle('body','tire','seat','bell')
hercules.work()