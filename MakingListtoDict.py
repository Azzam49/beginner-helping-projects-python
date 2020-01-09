#! python3
# making a dict from the list


def make_dict(theList):
    theDict = {}
    count = 1
    for item in theList:
        theDict[count] = item
        count += 2
    return theDict


myList = [55, 66, 88, 99]


print(make_dict(myList))
# Outputs : {1: 55, 2: 66, 3: 88, 4: 99}

#=============================================================================

# make a dict from the list, where the dict key
# is the 2nd item and its value is the 1st item from the list


myList2 = [55, 1, 66, 2, 88, 3, 99, 4]

def make_dict2(theList):
    theDict = {}
    count = 0
    while count < len(theList) -1:
        dictKey = theList[count+1]
        dictValue = theList[count]

        theDict[dictKey] = dictValue

        count += 2
        
    return theDict

print(make_dict2(myList2))
# Outputs : {1: 55, 2: 66, 3: 88, 4: 99}











