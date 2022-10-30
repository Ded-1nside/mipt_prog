from itertools import permutations


def get_permutations(s, n):
    ans = sorted(list(permutations(s, n)))
    for i in range(len(ans)):
        ans[i] = ''.join(list(ans[i]))
    return ans

#print(get_permutations("cat", 2))