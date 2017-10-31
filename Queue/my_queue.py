import random


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q=Queue()
    print (q.isEmpty())
    print (q.enqueue('dog'))
    print (q.enqueue(4))
    q = Queue()
    print (q.isEmpty())
    print (q)


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()
    return simqueue.dequeue()

if __name__ == "__main__":
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


