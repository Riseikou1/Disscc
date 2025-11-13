a = range(1, 5)
b = list(map(chr, range(ord('a'), ord('h') + 1)))

def setout(a) :
    if len(a) == 0 :
        print("\u2205")
        return 
    print("{", end = "")
    for i in range(len(a)) :
        if (i < len(a)- 1) :
            print(a[i], ", ", end = "", sep= "")
    print(a[i], "\b}\n")

print("A = ", end = "")
setout(a)

print("B = ", end = "")
setout(b)

print("\nA \u2a2f B = {", end = "")
for i in a :
    for j in b :
        print("(%d, %c), " %(i, j), end = " ")
print("\b\b\b}\n")
