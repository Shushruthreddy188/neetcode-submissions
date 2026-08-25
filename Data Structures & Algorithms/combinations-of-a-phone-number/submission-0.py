class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        cur = []

        def backtrack(i):
            if i == len(digits):
                res.append("".join(cur))
                return

            for ch in mapping[digits[i]]:
                cur.append(ch)
                backtrack(i + 1)
                cur.pop()

        backtrack(0)
        return res