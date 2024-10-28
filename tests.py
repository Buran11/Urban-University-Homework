import threading
import time
from queue import Queue


class MyThead(threading.Thread):
    def __init__(self, delay):
        super().__init__()
        self.delay = delay
        self.count = 0

    def run(self):
        while self.count < 3:
            time.sleep(self.delay)
            self.count += 1
            print(threading.current_thread().name, ' - ', self.count)


q = Queue(maxsize=3)
