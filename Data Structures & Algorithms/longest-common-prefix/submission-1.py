class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in range(len(strs[0])):
            cur = strs[0][i]
            for j in range(1,len(strs)):
                if i == len(strs[j]) or cur != strs[j][i]:
                    return strs[0][:i]

        return longest