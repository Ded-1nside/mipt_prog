from itertools import groupby


def compress_string(s):
    my_group = groupby(s)
    ans = []
    for i in my_group:
        ans.append((len(list(i[1])), int(i[0])))
    return ans


#print(compress_string('1222311'))