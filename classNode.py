class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)

        if not self.tail:
            self.tail = temp

        self.head = temp

    def add_2(self, item):
        new = Node(item)

        if self.tail:
            self.tail.setNext(new)

        if not self.head:
            self.head = new

        self.tail = new

    def append(self, item):
        new_node = Node(item)

        current = self.head
        last_node = None

        while current is not None:
            last_node = current
            current = current.getNext()

        if last_node:
            last_node.setNext(new_node)
        else:
            self.head = new_node


    def size(self):
        current = self.head
        count = 0
        while current is not None:
            print (current)
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found


    def index(self, item):
        index = 0
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
                break
            else:
                found = False
                index = index + 1
                current = current.getNext()
        if found is False:
            return -1


        return index


    def insert(self, index, char):
        current = self.head
        new_node = Node(char)
        previous = None

        i = 0
        while current is not None:
            data = current.getData()

            if i == index:
                new_node.setNext(current)
                break
            else:
                previous = current
                current = current.getNext()

            i = i + 1

        if previous:
            previous.setNext(new_node)
        else:
            self.head = new_node

        return

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if current == self.tail:
            self.tail = previous
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def pop(self, index=None):
        current = self.head
        previous = None
        found = False
        count = 0
        if index is None:
            index = self.size() - 1
        while not found:
            if count == index:
                found = True
            else:
                previous = current
                current = current.getNext()
            count += 1
        if current == self.tail:
            self.tail = previous
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        print (current.getData())


    def print_list(self):
        current = self.head
        data = []

        while current:
            data.append(current.getData())
            current = current.getNext()

        print (data)



mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
print (mylist.search(17))
print (mylist.size())
mylist.print_list()


# mylist = UnorderedList()
#
# mylist.append(31)
# mylist.append(77)
# mylist.append(17)
# mylist.append(93)
# mylist.append(26)
# mylist.append(54)

print (mylist.search(17))
print (mylist.size())
mylist.print_list()
print (mylist.index(93))
mylist.insert(0, 13)
mylist.insert(66, 13)
mylist.print_list()
mylist.remove(54)
mylist.print_list()
mylist.remove(13)
mylist.print_list()
mylist.remove(13)
mylist.print_list()
mylist.append(13)
mylist.print_list()
mylist.add_2(999)
mylist.add_2(88)
mylist.add_2(34)
mylist.print_list()
mylist.pop(0)
mylist.print_list()
mylist.pop(1)
mylist.print_list()
mylist.pop(2)
mylist.print_list()
mylist.pop(4)
mylist.print_list()
mylist.pop()
mylist.print_list()

