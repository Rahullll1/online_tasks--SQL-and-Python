from collections import defaultdict
def group_anagrams(words):
    res = defaultdict(list)
    for word in words:
        res[tuple(sorted(word))].append(word)
    return list(res.values())