'''
Write a function named letter_counter that takes a string as a
parameter and prints out the number of times each letter (upper- or lower-case)
appears in the string. The letters must be printed alphabetically and in lowercase.
You may use only strings and lists and their methods (i.e., dictionaries are not
allowed).
For example:
>>> letter_counter("brontasauruS")
The letter a is in the string brontasauruS 2 time(s).
The letter b is in the string brontasauruS 1 time(s).
The letter n is in the string brontasauruS 1 time(s).
The letter o is in the string brontasauruS 1 time(s).
'''

##def letter_counter(lst):
##    import string
##    count = 0
##  #  word = str(lst)
##   # letter = "abcdefghijklmnopqrstuvwxyz"
##    alphabet = string.ascii_lowercase
##    for letter in alphabet:
##        count += 1
##        lst.count(letter)
##    print(count)

import string
lowerLetters = string.ascii_lowercase

def letter_counter(word):
    for letter in lowerLetters:
        count = word.lower().count(letter)
        if count > 0:
            print(f"{letter} appears {count} times in {word}")
        
        
letter_counter("brontasauruS")














