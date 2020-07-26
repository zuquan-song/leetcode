import queue

class Solution:
    def calculate(self, s):
        def helper(q):
            sumVal, num, prev, prevOp = 0, 0, 0, '+'
            while not q.empty():
                ch = q.get()
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    num = helper(q)
                else:
                    if prevOp == '+':
                        sumVal += prev
                        prev = num
                    elif prevOp == '-':
                        sumVal += prev
                        prev = -num
                    elif prevOp == '*':
                        prev = prev * num
                    elif prevOp == '/':
                        prev = int(prev / num)
                    if ch == ')':
                        break
                    prevOp = ch
                    num = 0
            return prev + sumVal
        q = queue.Queue()
        for ch in s:
            if ch == ' ':
                continue
            q.put(ch)
        q.put(' ')
        return helper(q)