from itertools import combinations


def get_combinations(s, n):
    ans = []
    for i in range(1, n+1):
        cur = list(combinations(s, i))
        for j, elem in enumerate(cur):
            cur[j] = "".join(elem)
        ans.extend(cur)
    return ans

print(get_combinations("cat", 2))