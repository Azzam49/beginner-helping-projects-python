def compress(String):
    List1 = [i for i in String]
    List2 = []
    Count = []
    String2 = ""
    String3 = ""
    
    for i in List1:
        if i in List2:
            continue
        else:
            List2.append(i)

    for i in List2:
        count = List1.count(i)
        Count.append(str(count))
    
    for (letter,counT) in zip(List2,Count):
            String2 += letter + count

    for i in String2:
        if i == "1":
            continue
        else:
            String3 += i
    print(f"List 1 : {List1}")
    print(f"List 2 : {List2}")
    print(f"Count : {Count}")
    print(String2)

compress("abc")
# Output : a2b2c2d2
