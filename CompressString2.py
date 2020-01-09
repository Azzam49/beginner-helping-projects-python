#! python3

'''
Write a function named compress that takes a string as a parameter.
This function compresses a string by replacing any sequentially repeated letters
with a letter and a number where the number indicates how many times the letter
was repeated. The function returns the compressed string.
For example:
>>> compress("")
''
>>> compress("abc")
'abc'
>>> compress("aabbbccccc")
'a2b3c5'
'''

def compress(String):
    List1 = [i for i in String]
    #List2 = list(set(List1))
    List2 = []
    String2 = ""
##    String3 = ""
    
    for i in List1:
        if i in List2:
            continue
        else:
            List2.append(i)
            
    for letter in List2:
        count = List1.count(letter)
        String2 += letter + str(count)
        
    print(String2)

##    for i in range(len(String)):
##        
##        String3 += String[i]
        
compress("aabbccaa")
# Output shall be : a2b2c2a2 and not a4b2c2

##    for i in List2:
##        count = List1.count(i)
##        Count.append(str(count))

##    for (letter,count) in zip(List2,Count):
##        String2 += letter + "(" + count + ")"
        
##    print(List1)
   
##    print(Count)
##    print(String2)
    

         
##while True:
##    User_input = input("Your String : ")
##    print("Compressed String : " + compress(User_input))
##    print("\n")

    
##def compress(String):
##    List = list(String)
##    Dict = {i:0 for i in List}
##    Sent = ""
##    
##    for i in List:
##        if i in Dict.keys():
##            Dict[i] += 1
##
##    for key,value in Dict.items():
##        Sent += str(key)
##        Sent+= str(value)
##        
##    print(List) # For checking 
##    print(Dict) # For checking
##    print(Sent) # Our Result
##
##compress("aabbcZZZxxyyy")
