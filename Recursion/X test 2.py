def tri_recursion(k):
    if(k>0):
        print("Y")
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    print("X") 
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
