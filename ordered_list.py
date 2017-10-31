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

    def __repr__(self):
        text = "Node: value=%s" % self.getData()

        next = self.getNext()

        if next:
            text += ' next Node: value=%s' % next.getData()

        return text

        
class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found



    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(current) #self.head
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def print_list(self):
        data = []
        current = self.head
        while current:
            data.append(current.getData())
            current = current.getNext()
        print (data)


my_list = OrderedList()
my_list.add(12)
my_list.add(66)
my_list.add(34)
my_list.add(45)
my_list.add(11)
my_list.add(67)
my_list.add(0)
my_list.add(2)
my_list.add(-1)
my_list.print_list()
print (my_list.search(67))
