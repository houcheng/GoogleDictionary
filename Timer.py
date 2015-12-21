import time, threading

class TimerTask:
    def doJob(self):
        print ("null timer task")

class Timer:
    def __init__(self, timeout):
        self.timeout = timeout
        self.timer = None
    def schedule(self, task):
        self.task = task
        self.cancel_timer()
        self.start_timer()
    def cancel_timer(self):
        if self.timer != None:
            self.timer.cancel()
    def start_timer(self):
        self.timer = threading.Timer(self.timeout, self.task.doJob)
        self.timer.start()

