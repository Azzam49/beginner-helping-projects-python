# An example of a recursive function to
# find the factorial of a number
##
##def calc_factorial(x):
##    """This is a recursive function
##    to find the factorial of an integer"""
##
##    if x == 1:
##        return 1
##    else:
##        #print(x * calc_factorial(x-1))
##        return (x * calc_factorial(x-1))
##
##num = 4
##print("The factorial of", num, "is", calc_factorial(num))		
#============================================================
def tri_recursion(k):
    if (k>0):
               
        result = k+tri_recursion(k-1)
        
        print("result ",result)
    
    else:
        result = 0
    return result
    
print("Recursion Example Results")
tri_recursion(6)

# An example of a recursive function to
# find the factorial of a number

##def calc_factorial(x):
##    """This is a recursive function
##    to find the factorial of an integer"""
##
##    if x == 1:
##        return 1
##    else:
##        return (x * calc_factorial(x-1))
##
##num = 4
##print("The factorial of", num, "is", calc_factorial(num))		
#==============================================================
# The factorial of 4 is 24
#==============================================================
'''
Python Recursive Function
We know that in Python, a function can call other functions. It is even possible for the function to call
itself. These type of construct are termed as recursive functions.

Following is an example of recursive function to find the factorial of an integer.

Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial
of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

Example of recursive function
script.py
IPython Shell


Run
Powered by DataCamp

In the above example, calc_factorial() is a recursive functions as it calls itself.

When we call this function with a positive integer, it will recursively call itself by decreasing
the number.

Each function call multiples the number with the factorial of number 1 until the number is equal to one.
This recursive call can be explained in the following steps.


calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
Our recursion ends when the number reduces to 1. This is called the base condition.

Every recursive function must have a base condition that stops the recursion or else the function
calls itself infinitely.

Advantages of Recursion
Recursive functions make the code look clean and elegant.
A complex task can be broken down into simpler sub-problems using recursion.
Sequence generation is easier with recursion than using some nested iteration.
'''
#==============================================================
# The factorial of 4 is 24
#==============================================================

##
##def calc_factorial(x):
##    """This is a recursive function
##    to find the factorial of an integer"""
##
##    if x == 1:
##        return 1
##    else:
##        return (x * calc_factorial(x-1))
##
##num = 4
##print("The factorial of", num, "is", calc_factorial(num))





##import keyboard
##
##while True:
##    # Recognize up key if pressed 
##    if keyboard.is_pressed('up'): 
##        print('You pressed the Up key!')
##        break 
##    else:
##        pass
