
def combine_line(lines):
    lines.sort(key=lambda x: (x[0], x[1]))
    res = []
    for line in lines:
        if not len(res) or res[-1][1] < line[0]:
            res.append(line)
        else:
            if res[-1][1] < line[1]:
                begin, end, val = res.pop()
                if begin == line[0]:
                    res.append((begin, end, val + line[2]))
                    res.append((end, line[1], line[2]))
                else:
                    res.append((begin, line[0], val))
                    res.append((line[0], end, val + line[2]))
                    res.append((end, line[1], line[2]))
            else:
                begin, end, val = res.pop()
                if begin == line[0] and end == line[1]:
                    res.append((begin, end, val + line[2]))
                elif begin == line[0]:
                    res.append((line[0], line[1], val + line[2]))
                    res.append((line[1], end, val))
                elif end == line[1]:
                    res.append((begin, line[0], val))
                    res.append((line[0], end, val + line[2]))
                else:
                    res.append((begin, line[0], val))
                    res.append((line[0], line[1], val + line[2]))
                    res.append((line[1], end, val))
    return res

if __name__ == '__main__':
    print(combine_line([(1,4,5), (3,8,-5), (10,12,2), (10,12,4)]))