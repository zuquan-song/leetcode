
req = [False, False]
turn = 0

def peterson_1():
    while True:
        req[0] = True
        turn = 1
        while req[1] and turn == 1:
            pass
        # ... critical section
        req[0] = False

def peterson_2():
    while True:
        req[1] = True
        turn = 0
        while req[0] and turn == 0:
            pass
        # ... critical section
        req[1] = False
