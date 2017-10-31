import re


def list_sum(numList):
    if len(numList) == 1:
        res = numList[0]
        return res
    else:
        res = numList[0] + list_sum(numList[1:])
    return res

print(list_sum([1,3,5,7,9]))


def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]


   # Convert number to string using Stack
def _toStr(n,base):
    stack_list = []
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            stack_list.append(convertString[n])
        else:
            stack_list.append(convertString[n % base])
        n = n // base
    res = ''
    while stack_list:
        res += str(stack_list.pop())
    return res


print(_toStr(1453,16))

def reverse_str(str_to_reverse):
    if len(str_to_reverse) == 1:
        return str_to_reverse
    else:
        return reverse_str(str_to_reverse[1:]) + str_to_reverse[0]

print (reverse_str('lion'))


def _is_palindrom(words):
    if len(words) == 1:
        return True
    else:
        if words[0] == words[len(words)-1]:
            return is_palindrom(words[1:len(words) - 1])
        else:
            return False


def is_palindrom(words):
    words = re.sub(r'[\.,\s]', '', words).lower()

    return _is_palindrom(words)



print (is_palindrom('Kanakanak'))
print(_toStr(1453,16))


def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search(alist[:midpoint], item)
            else:
                if item > alist[midpoint]:
                    return binary_search(alist[midpoint + 1:], item)




testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print (binary_search(testlist, 3))
print (binary_search(testlist, 13))



