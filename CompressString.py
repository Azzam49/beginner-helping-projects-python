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
    List = list(String)
    Dict = {i:0 for i in List}
    Sent = ""
    
    for i in List:
        if i in Dict.keys():
            Dict[i] += 1

    for key,value in Dict.items():
        Sent += str(key)
        Sent+= str(value)
        
    print(List) # For checking 
    print(Dict) # For checking
    print(Sent) # Our Result

compress("aabbcZZZxxyyy")
