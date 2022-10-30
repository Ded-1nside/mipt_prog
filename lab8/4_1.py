from itertools import combinations_with_replacement


def get_combinations_with_r(s, n):
    ans = sorted(list(combinations_with_replacement(s, n)))
    for i, elem in enumerate(ans):
        ans[i] = "".join(sorted(elem))
    return ans


#print(get_combinations_with_r("cat", 2))