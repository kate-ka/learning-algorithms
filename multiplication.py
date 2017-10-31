def multiply(x, y):
    a = int(x[0:len(x)/2])
    b = int(x[(len(x)/2):])
    c = int(y[0:len(y)/2])
    d = int(y[(len(y)/2):])
    n = len(x)
    result = 10 ** n *a * c + 10 ** (n/2) * (a * d + b * c) + b * d
    return result

X = '1234'
Y = '5678'
print multiply(X, Y)


counter = 0

def karachuba(x, y):
    max_len = max(len(x), len(y))

    if len(x) < max_len:
        x = x.zfill(max_len)

    if len(y) < max_len:
        y = y.zfill(max_len)

    if len(y) == len(x) == 1:
        return int(x) * int(y)

    a = int(x[0:len(x)/2])
    b = int(x[(len(x)/2):])
    c = int(y[0:len(y)/2])
    d = int(y[(len(y)/2):])
    n = len(x)

    global counter

    # ad_bc = karachuba(str(a), str(d)) + karachuba(str(b), str(c))
    # print ad_bc
    # if ad_bc == 7:
    #     counter += 1
    #
    # print "lzz", ad_bc
    #result = 10 ** n * karachuba(str(a), str(c)) + 10 ** (n/2) * (ad_bc) + karachuba(str(b), str(d))

    ad_bc = karachuba(str((a + b)), str((c + d))) - karachuba(str(a), str(c)) - karachuba(str(b), str(d))
    print ad_bc
    return counter

print karachuba(X, Y)





