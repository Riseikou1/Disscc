def helper(lst, set_size) :
    print("P({", end = "")
    print(",".join(lst), end= "")
    print("}) = {(\u2205", end = "")
    for counter in range(1, 1 << set_size) :
        subset = [lst[i] for i in range(set_size) if counter & (1 << i)]
        print(",{" + ",".join(subset) + "}", end = "")
    print("}")

n = int(input("Enter natural number n : "))
lst = [str(i + 1) for i in range(n)]
helper(lst, n)
