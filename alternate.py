#! python3



##def alternate(list1,list2):
##    return zip(list1,list2)
##
##
##result = alternate([1,2],[4,5,6])
##
##print(list(result))

##def alternate(lst1, lst2):
##    lst3 = []
##
##    for i in range (0,len(lst1)):
##
##        if len(lst1) <=0:
##
##            return None 
##
##
##        for j in range (0,len(lst2)):
##            if len(lst2) <=0:
##
##                return None
##
##            if lst1[i] == lst2[j]:
##
##                lst3.append(i+1)
##
##                lst3.append(j+1)
##    print(lst3)
##
##
##alternate([1,2],[4,5])





def alternate(list1,list2):
    list3 = []
    i= 0
    x= 0
    while True:
        if i < len(list1):
            list3.append(list1[i])
            i +=1
        if x < len(list2):
            list3.append(list2[x])
            x +=1

        if int(len(list1)) + int(len(list2)) == int(len(list3)):
            break
        
    return list3


print(alternate([1,2,"a","b","x","s"],[4,5,"b","v"]))
# output : [1, 4, 2, 5, 'a', 'b', 'b', 'v', 'x', 's']















