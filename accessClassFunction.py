#! python3

class Math:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self,x,y):
        return self.num1 + x + y

M1 = Math(20,20)

def MyOutput():
    print("The result from add() function inside Math class is :" + str(M1.add(1,2)))


MyOutput()
