#=====================================================
# RECURSION DEFINATION
# Recursion : the repeating of an application.

# Recursion in python : Function calling itselff

# So this Recursive function is repeating itself, as it call it self
# again and again. as a For loop,but it have limit of 1000 loops.

# This is infinite loop until reaches the default limit.
def greet():
    print("Hello")
    greet()

greet()


# You can change the default 1000 recusrion limit by sys module.
# import sys
# sys.setrecursionlimit(2000)
# To know your current recursion limit : print(sys.getrecursionlimit())
# So now recursion limit is 2000.
#=====================================================




#=====================================================
# FACTORIAL DEFNATION
# Factorial of 5 is : 5*4*3*2*1 : 120 \ 5! = 5 * 4!
# 0 factorial is : 1 , 1 factorial is : 1 . \ (0!=1, 1!=1)
