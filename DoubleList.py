

List = ["Hello","wassup","sup"]
List2 = []

def DoubleList(lst):
    for i in lst:
        List2.append(i)
        List2.append(i)
    List1 = List2
    print(List1)
    
DoubleList(List)
# Output : ['Hello', 'Hello', 'wassup', 'wassup', 'sup', 'sup']
#================

List = [i+i for i in List]
print(List)
# Output : ['HelloHello', 'wassupwassup', 'supsup']
