
for i in range(5):
    print("1")
    print("2")
print("===========")

def tri(x):
        
    if x > 0:
    #    result = x+tri(x-1)
#        print(result)
    #    return x+tri(x-1)
        #print(x+tri(x-1))
        print("1")
        print("2")
        return x+tri(x-1)
        
    else:
        return 0
        #x = 0
    
print(tri(5))
        


##def oo(x):
##
##    if x > 0:
##        print("hello")
##        x -= 1
##        oo(x)
##        
##oo(4)
