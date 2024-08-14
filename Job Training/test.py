from typing import DefaultDict, List


def solution(strs: List[str]) -> List[List[str]]:
    ans = DefaultDict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))
        ans[sorted_word].append(word)

    return list(ans.values())


solution(["act", "pots", "tops", "cat", "stop", "hat"])
