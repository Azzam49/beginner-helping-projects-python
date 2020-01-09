
def loops(start,stop,step,lst):
   for i in range(start,stop,step):
        if step >= 1 and start < stop:
                print(lst[i], end = " ")
        elif start > stop:
            start,stop = stop, start
            print(lst[[start,stop]])
            print(lst[i], end = " ")



loops(1,10,2,[1,2,3,4,5])
