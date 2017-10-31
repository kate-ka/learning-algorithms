
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
print(s)

def revstring(mystr):
    myStack = Stack()
    for ch in mystr:
        myStack.push(ch)
    revstr = ''
    while not myStack.isEmpty():
        revstr += myStack.pop()

    return revstr


print (revstring('apple'))
print (revstring('1234567890'))


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                       balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))


def parChecker(symbolString):
    stack = []
    close_brackets = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    balanced = True
    for ch in symbolString:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            expected_open_brac = close_brackets[ch]

            if not stack or expected_open_brac != stack[len(stack)-1]:
                balanced = False
                break
            else:
                stack.pop()
    if stack:
        balanced = False
    return balanced


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))
print(parChecker('()[)])'))
print(parChecker('(()'))