import queue
import threading
import time


class ExecService(threading.Thread):
    def __init__(self, queue, *args, **kwargs):
        self.queue = queue
        super().__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(.5)
            self.queue.put('1')

queue = queue.Queue()
service = ExecService(queue)

service.start()

while True:
    if not queue.empty():
        print(queue.get())

service.join()
