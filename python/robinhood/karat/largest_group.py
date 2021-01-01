from copy import copy
import collections

def permutation(names):
    n = len(names)
    for i in range(1, 2 ** n):
        cand = []
        while i > 0:
            if i & 1:
                cand.append(names[i])
            i = i >> 1
        yield ",".join(cand)

def largest_group(records):
    records.sort(key=lambda x: int(x[1]))

    for r in records:
        print(r)
    names, times = set(), set()
    group_with_periods = collections.defaultdict(list)
    for record in records:
        name, time, status = record[0], int(record[1]), record[2]
        if status == "enter":
            names.add(name)
            times.add(time)
        else:

            names.remove(name)
            times.remove(name)

    mx = float('-inf')
    final_group, final_period = "", ""
    for group, periods in group_with_periods.items():
        # print(group, periods)
        if len(periods) >= 2 and len(group.split(",")) > mx:
            mx = len(group.split(","))
            final_group = group
            final_period = ",".join(periods)
    return "{}: {}".format(final_group, final_period)



badge_records = [
  ["Paul",     "1214", "enter"],
  ["Paul",      "830", "enter"],
  ["Curtis",   "1100", "enter"],
  ["Paul",      "903", "exit"],
  ["John",      "908", "exit"],
  ["Paul",     "1235", "exit"],
  ["Jennifer",  "900", "exit"],
  ["Curtis",   "1330", "exit"],
  ["John",      "815", "enter"],
  ["Jennifer", "1217", "enter"],
  ["Curtis",    "745", "enter"],
  ["John",     "1230", "enter"],
  ["Jennifer",  "800", "enter"],
  ["John",     "1235", "exit"],
  ["Curtis",    "810", "exit"],
  ["Jennifer", "1240", "exit"],
]

print(largest_group(badge_records))