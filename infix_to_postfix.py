def infixToPostfix(infixexpr):
    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opstack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            if opstack:
                while opstack and prec[opstack[len(opstack) - 1]] >= prec[token]:
                    postfixList.append(opstack.pop())
            opstack.append(token)

    while opstack:
        postfixList.append(opstack.pop())
    return " ".join(postfixList)



print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("( A + B ) * ( C + D )"))
#'A B + C D + *'
print (infixToPostfix("( A + B ) * C"))
#'A B + C *'
print (infixToPostfix(("A + B * C")))
#'A B C * +'
print(infixToPostfix(" 5 * 3 ^ ( 4 - 2 )"))

