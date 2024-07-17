import time


class Timer:
    def __init__(self):
        self.s_time = time.time()
        self.e_time = time.time()

    def start(self):
        self.s_time = time.time()

    def end(self):
        self.e_time = time.time()

    def print(self):
        print(format(self.e_time - self.s_time, ".10f"))
