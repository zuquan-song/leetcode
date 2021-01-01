from threading import Semaphore
from typing import Callable

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.counter = 1
        self.nb = Semaphore(1)
        self.fz = Semaphore(0)
        self.bz = Semaphore(0)
        self.fzbz = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                self.fz.acquire()
                printFizz()
                self.releaseLock(i + 1)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                self.bz.acquire()
                printBuzz()
                self.releaseLock(i + 1)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                self.fzbz.acquire()
                printFizzBuzz()
                self.releaseLock(i + 1)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                self.nb.acquire()
                printNumber(i)
                self.releaseLock(i + 1)

    def releaseLock(self, i):
        if i == self.n + 1:
            return
        if i % 3 == 0 and i % 5 != 0:
            self.fz.release()
        elif i % 3 != 0 and i % 5 == 0:
            self.bz.release()
        elif i % 3 == 0 and i % 5 == 0:
            self.fzbz.release()
        else:
            self.nb.release()

if __name__ == '__main__':
    import threading
    fb = FizzBuzz(10)
    t1 = threading.Thread(target=fb.fizz, args=(lambda : print("fizz"), ))
    t2 = threading.Thread(target=fb.buzz, args=(lambda : print("buzz"), ))
    t3 = threading.Thread(target=fb.fizzbuzz, args=(lambda : print("fizzbuzz"), ))
    t4 = threading.Thread(target=fb.number, args=(lambda x: print("{}".format(x)), ))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()