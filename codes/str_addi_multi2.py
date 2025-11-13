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
    digits = ""
    res = []

    while num != "0" :
        num, rem = divide(num, base)
        res.append(digits[rem])

    return "".join(reversed(res) if res else "0")
