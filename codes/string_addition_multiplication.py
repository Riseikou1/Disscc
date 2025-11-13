def main() :
    binary = input("Enter the binary number : ")
    decimal = "0"
    multiplier = "1"
    for b in reversed(binary) :
        if b == '1' :
            decimal = addStrings(decimal, multiplier)
        multiplier = multiply(multiplier, "2")

    print("decimal : ", decimal)

    octal = toBase(decimal, 8)
    print("Octal : ", octal)

    hexa = toBase(decimal, 16)
    print("Hexadecimal : ", hexa)

def addStrings(num1, num2) :
    res = []
    carry = 0
    p1, p2 = len(num1) - 1, len(num2) - 1

    while p1 >= 0 or p2 >= 0 or carry :
        digit1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        digit2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
        total = digit1 + digit2 + carry
        carry, value = divmod(total, 10)
        res.append(value)
        p1 -= 1
        p2 -= 1
    
    return "".join(str(digit) for digit in reversed(res))

def multiply(num1, num2) :
    n = len(num1) + len(num2)
    res = [0] * n
    carry = 0
    first_num = num1[::-1]
    second_num = num2[::-1]

    for idx2, digit2 in enumerate(second_num) :
        for idx1, digit1 in enumerate(first_num) :
            idx = idx2 + idx1 
            carry = res[idx]
            multiplication = int(digit1) * int(digit2) + carry
            res[idx] = multiplication % 10
            res[idx + 1] += multiplication // 10

    if res[-1] == 0 :
        res.pop()

    return "".join(reversed(res))

def divide(num, base) :
    quotient = []
    remainder = 0
    for digit in num :
        remainder = remainder * 10 + int(digit)
        q, remainder = divmod(remainder, base)
        if quotient or q != 0 :
            quotient.append(str(q))
    return ("".join(quotient) if quotient else "0", remainder)

def toBase(num, base) :
    digits = "0123456789ABCDEF"
    res = []
    while num != "0" :
        num, rem = divide(num, base)
        res.append(digits[rem])
    return "".join(reversed(res)) if res else "0"


if __name__ == "__main__" :
    main()
