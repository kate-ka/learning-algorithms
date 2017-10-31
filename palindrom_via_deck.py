def palchecker(aString):
    chardeque = []

    for char in aString:
        chardeque.insert(0, char)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop(0)
        last = chardeque.pop()
        if first != last:
            stillEqual = False
    return stillEqual

print(palchecker('radar'))