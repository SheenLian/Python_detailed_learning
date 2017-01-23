
import threading
import time


'''high level threading'''


def print_time(thread, delay, counter):
    while counter:
        if exitflag:
            break
        time.sleep(delay)
        print('%s: %s' % (thread, time.asctime()))
        counter -= 1


exitflag = 0


class Thread(threading.Thread):
    def __init__(self, thread, name, delay):
        threading.Thread.__init__(self)
        self.thread = thread
        self.name = name
        self.delay = delay

    def run(self):
        print('>Starting ' + self.name)
        print_time(self.name, self.delay, 5)
        print('>Exiting ' + self.name)




thread_1 = Thread(1, 'Sheen', 1)
thread_2 = Thread(2, 'Lily', 2)

thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
