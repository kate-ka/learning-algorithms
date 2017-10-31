import random

class Printer(object):

    def __init__(self, pages_per_minute):
        self.pages_per_minute = pages_per_minute
        self.current_task = None

    def set_task(self, task):
        """
        Set task to print. it means printer will start to print this task
        """
        self.current_task = task
        self.remain_time = task.get_pages() / self.pages_per_minute * 60

    def is_busy(self):
        if self.current_task:
            return True
        else:
            return False

    def tick(self):
        if self.current_task:
            self.remain_time = self.remain_time - 1

            if self.remain_time <= 0:
                self.current_task = None

class Task(object):
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.pages_to_print = random.randrange(1,21)

    def get_pages(self):
        return self.pages_to_print

    def get_wait_time(self, current_time):
        return current_time - self.timestamp


def student_wants_to_print_document():
    num = random.randrange(1,181)

    if num == 180:
        return True
    else:
        return False



def simulate(period_sec, pages_per_minute):
    task_queue = []
    printer = Printer(pages_per_minute)
    wait_time = []


    for current_second in range(period_sec):
        if student_wants_to_print_document():
            task = Task(current_second)
            task_queue.insert(0, task)

        if not printer.is_busy() and task_queue:
            task = task_queue.pop()
            wait_time.append(task.get_wait_time(current_second))
            printer.set_task(task)

        printer.tick()

    print 'average wait time %s s' % (sum(wait_time)/ len(wait_time))

for i in range(10):
    simulate(3600, 5)