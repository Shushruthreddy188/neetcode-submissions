class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(part.copy())
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    part.append(s[start:end + 1])

                    backtrack(end + 1)

                    part.pop()

        backtrack(0)
        return res