def helper(lst, set_size) :
    pow_set_size = 1 << set_size
    counter = 0
    j = 0
    print("P({", end = "")
    for i in range(set_size) :
        if i == set_size - 1 :
            print(lst[i], end = "")
        else :
            print(lst[i], end = ",")
    print("}) = { \u2205", end = "")
    for counter in range(1, pow_set_size) :
        print(",{", end = "")
        for j in range(set_size) :
            if(counter & (1 << j)) > 0 :
                print(lst[j], end = ",")
        print("\b}", end = "")
    print("}")

n = int(input("Enter natural number n : "))
lst = []
for i in range(n) :
    lst.append(str(i + 1))
helper(lst, n)
print()