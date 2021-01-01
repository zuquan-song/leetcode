import functools

def grouping_options(people, groups):

    @functools.lru_cache(None)
    def dfs(prev, remain_people, remain_group):
        if remain_group == 0:

            return 1 if remain_people == 0 else 0
        res = 0
        for i in range(prev, remain_people // remain_group + 1):
            if remain_people - i >= 0:
                res += dfs(i, remain_people - i, remain_group - 1)
        return res
    counter = dfs(1, people, groups)
    return counter

print(grouping_options(4, 2))