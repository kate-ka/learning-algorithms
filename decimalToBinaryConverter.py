def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    remainder = []
    while decNumber > 0:
        remainder.append(decNumber % base)
        decNumber = decNumber / base
    result = ''
    while remainder:
        result += digits[remainder.pop()]
    return result

print(baseConverter(26, 26))