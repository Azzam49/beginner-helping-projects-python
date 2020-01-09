#! python3
'''
Question
[30 marks] Write a function named expand that takes a string in the compressed
format and returns the original string. You may assume that any number in the
compressed string is a single-digit number.
For example:
>>> expand("")
''
>>> expand("abc")
'abc'
>>> expand("a3b7c2")
'aaabbbbbbbcc'
'''

##def Expand(String):
##    Return = ""
##    
##    for i in range(len(String)):
##
##        if i != max(1,len(String)):
##            if String[i+1].isdigit() == True:
##                Return += String[i] * int(String[i+1])
##                print(Return)
##            else:
##                Return += String[i]
##                print(Return)
##    print(Return)
##
##Expand("a3b7c2")



def Expand(String):
    Return = ""
    i = 0
    while True:
        
        if String[i].isdigit() == True:
            Return += String[i-1] *2
            
        Return += String[i]
        
        if Return[i] == String[-2]:
            break
        i += 1
        
    print(Return)
   
Expand("a3b7c2")







