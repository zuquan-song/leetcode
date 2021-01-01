
from threading import Semaphore
from typing import Callable

class DiningPhilosophers:

    def __init__(self):
        self.locks = [Semaphore(1) for _ in range(5)]
        self.semaphore = Semaphore(4)

    def pick_fork(self, i, pick):
        self.locks[i].acquire()
        pick()

    def put_fork(self, i, put):
        put()
        self.locks[i].release()

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left, right = philosopher, (philosopher + 4) % 5
        self.semaphore.acquire()

        self.pick_fork(left, pickLeftFork)
        self.pick_fork(right, pickRightFork)
        eat()
        self.put_fork(right, putLeftFork)
        self.put_fork(left, putRightFork)
        self.semaphore.release()
