def main() :
    binary = input("Enter a binary number : ")
    ans = "0"
    multiplier = "1"
    for b in reversed(binary) :
        if b == "1" :
            ans = addStrings(ans, multiplier)
        multiplier = multiply(multiplier, "2")

    print("Decimal representation is : ", ans)

def addStrings(num1, num2) :
    p1, p2 = len(num1) - 1, len(num2) - 1
    carry = 0
    res = []
    while p1 >= 0 or p2 >= 0 or carry :
        digit1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        digit2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
        total = digit1 + digit2 + carry
        carry, value = divmod(total, 10)
        res.append(str(value))
        p1 -= 1
        p2 -= 1
    return "".join(reversed(res))

def multiply(num1, num2) :
    N = len(num1) + len(num2)
    ans = [0] * N
    first_number = num1[::-1]
    second_number = num2[::-1]

    for place2, digit2 in enumerate(second_number) :
        for place1, digit1 in enumerate(first_number) :
            idx = place1 + place2
            carry = ans[idx]
            multiplication = int(digit1) * int(digit2) + carry
            ans[idx] = multiplication % 10
            ans[idx + 1] += multiplication // 10
    
    if ans[-1] == 0 :
        ans.pop()

    return "".join(str(digit) for digit in reversed(ans))

if __name__ == "__main__" :
    main()

