import collections

def goodTuple(array):
    result = 0
    for i in range(2, len(array)):
        counters = collections.Counter(array[i-2: i+1])
        if len(counters) == 2:
            result += 1
    return result

def sumOfString(a, b):
    a, b = a, b if len(a) < len(b) else b, a
    res = ""
    for i in range(len(a)):
        res += str(int(a) + int(b))
    return res

def divideTwoArray(array):
    array.sort()
    j = 0
    arrayA, arrayB = [], []
    counters = collections.Counter(array)
    for num, cnt in counters.items():
        if cnt > 2:
            return None
        elif cnt == 2:
            arrayA.append(num)
        else:
            [arrayA, arrayB][len(arrayA) > len(arrayB)].append(num)
    return arrayA, arrayB

def coolFeature(a, b, querys):
    counterA = collections.Counter(a)
    counterB = collections.Counter(b)
    result = []
    for query in querys:
        if len(query) == 2:
            _, target = query[0], query[1]
            for key, val in counterA.items():
                if target - key in counterB:
                    result[-1] += min(val, counterB[key])
        else:
            _, idx, num = query[0], query[1], query[2]
            counterB[b[idx]] -= 1
            counterB[num] += 1
            b[idx] = num
    return result



def divisorSubString(a, b):
  if len(a) != len(b) or len(set(a).difference(set(b))) != 0:
    return False
  
  cntA, cntB = collections.Counter(a), collections.Counter(b)

  revCntA, revCntB = collections.defaultdict(int), collections.defaultdict(int)
  for _, val in revCntA:
    revCntA[val] += 1
  for _, val in revCntB:
    revCntA[val] -= 1
  
  return all([val == 0 for val in revCntA.values()])


