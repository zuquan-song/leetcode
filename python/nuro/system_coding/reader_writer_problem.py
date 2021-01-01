from threading import Semaphore, Condition



class ReaderWriter:

    def __init__(self):
        self.rw_mutex = Semaphore(1)
        self.mutex = Semaphore(1)
        self.read_count = 0

    def write(self, data):
        while True:
            self.rw_mutex.acquire()
            # do writing
            self.rw_mutex.release()

    def read(self):
        while True:
            self.mutex.acquire()
            self.read_count += 1
            if self.read_count == 1:
                # only first reader locks rw_mutex
                self.rw_mutex.acquire()
            self.mutex.release()

            # reading

            self.mutex.acquire()
            self.read_count -= 1
            if self.read_count == 0:
                self.rw_mutex.release()
            self.rw_mutex.release()


