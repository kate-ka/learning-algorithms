def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    # def __repr__(self):
    #     return str(self.num)+"/"+str(self.den)


    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)


    def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum


    def __mul__(self, other):
        firstnum = self.num * other.num
        secondnum = self.den * other.den
        return Fraction(firstnum, secondnum)


    def __div__(self, other):
        fnum = self.num * other.den
        snum = self.den * other.num
        commom = gcd(fnum, snum)
        return Fraction(fnum/commom, snum/commom)


    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)


    def __lt__(self, other):
        fnum = self.num * other.den
        snum = self.den * other.num
        return fnum < snum



    # def __radd__(self, otherfraction):
    #     if otherfraction == 0:
    #         return self
    #     elif isinstance(otherfraction, Fraction):
    #         return self.__add__(otherfraction)
    #     else:
    #         raise TypeError("Can't sum Fraction object with %s" % type(otherfraction))

# myfr= Fraction(3,5)
# print(myfr)
# print "I ate", myfr, "of pizza"
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
print (f1 < f2)


#f3 = sum([f1, f2])
#print f3

# def sum_our_fractions(result, current):
#     print 'res = %s' % result
#     print 'current = %s' % current
#     return result + current
#
# print reduce(sum_our_fractions, [f1, f2], 5)



