def main():
    binary = input("Enter a binary number: ")

    # Step 1: Binary → Decimal (already done)
    decimal = "0"
    multiplier = "1"
    for b in reversed(binary):
        if b == "1":
            decimal = addStrings(decimal, multiplier)
        multiplier = multiply(multiplier, "2")

    print("Decimal:", decimal)

    # Step 2: Decimal → Octal
    octal = toBase(decimal, 8)
    print("Octal:", octal)

    # Step 3: Decimal → Hexadecimal
    hexa = toBase(decimal, 16)
    print("Hexadecimal:", hexa)


def addStrings(num1, num2):
    p1, p2 = len(num1) - 1, len(num2) - 1
    carry = 0
    res = []
    while p1 >= 0 or p2 >= 0 or carry:
        digit1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
        digit2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
        total = digit1 + digit2 + carry
        carry, value = divmod(total, 10)
        res.append(str(value))
        p1 -= 1
        p2 -= 1
    return "".join(reversed(res))


def multiply(num1, num2):
    N = len(num1) + len(num2)
    ans = [0] * N
    first_number = num1[::-1]
    second_number = num2[::-1]

    for place2, digit2 in enumerate(second_number):
        for place1, digit1 in enumerate(first_number):
            idx = place1 + place2
            carry = ans[idx]
            multiplication = int(digit1) * int(digit2) + carry
            ans[idx] = multiplication % 10
            ans[idx + 1] += multiplication // 10

    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()

    return "".join(str(digit) for digit in reversed(ans))


def divide(num, base):
    """Divide big integer string 'num' by base, return (quotient, remainder)."""
    quotient = []
    remainder = 0
    for digit in num:
        remainder = remainder * 10 + int(digit)
        q, remainder = divmod(remainder, base)
        if quotient or q != 0:
            quotient.append(str(q))
    return ("".join(quotient) if quotient else "0", remainder)


def toBase(num, base):
    """Convert decimal string 'num' to base (8 or 16)."""
    digits = "0123456789ABCDEF"
    res = []
    while num != "0":
        num, rem = divide(num, base)
        res.append(digits[rem])
    return "".join(reversed(res)) if res else "0"


if __name__ == "__main__":
    main()
