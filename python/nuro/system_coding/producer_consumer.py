class MyCircularQueueArray:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.cap = k
        self.input = 0
        self.out = 0
        self.values = [0] * (k + 1)

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.input + 1) % len(self.values) == self.out:
            return False

        self.values[self.input] = value
        self.input = (self.input + 1) % len(self.values)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.out == self.input:
            return False
        val = self.values[self.out]
        self.out = (self.out + 1) % len(self.values)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.input == self.out:
            return -1

        i = self.out % len(self.values)
        return self.values[i]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.input == self.out:
            return -1

        i = (self.input - 1) % len(self.values)
        return self.values[i]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.input == self.out

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.input + 1) % len(self.values) == self.out

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()