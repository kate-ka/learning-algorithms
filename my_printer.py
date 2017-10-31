import random


class Printer(object):
    def __init__(self, pages_per_minute):
        self.pages_per_minute = pages_per_minute
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask:
            self.timeRemaining = self.timeRemaining - 1
        if self.timeRemaining <= 0:
            self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def set_task(self, task):
        self.currentTask = task
        self.timeRemaining = task.get_pages() * 60 / self.pages_per_minute




class Task(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.pages_to_print = random.randrange(1, 21)

    def get_pages(self):
        return self.pages_to_print

    def waittime(self, current_time):
        return current_time - self.timestamp



def student_wants_to_print():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False


def simulation(period, pages_per_minute):
    printer = Printer(pages_per_minute)
    queue_of_tasks = []
    timewait = []
    for current_second in range(period):

        if student_wants_to_print():
            new_task = Task(current_second)
            queue_of_tasks.insert(0, new_task)

        if not printer.busy() and queue_of_tasks:
            new_task = queue_of_tasks.pop()
            timewait.append(new_task.waittime(current_second))
            printer.set_task(new_task)

        printer.tick()
    print ('average time is %s' %(sum(timewait)/len(timewait)))


for i in range(10):
    simulation(3600, 5)





