class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(" ".join(path))
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    path.append(word)

                    backtrack(end)

                    path.pop()

        backtrack(0)
        return res