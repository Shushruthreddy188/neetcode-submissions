class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if ten != 0:
                    ten -= 1
                    if five < 1:
                        return False
                    else:
                        five -= 1
                else:
                    if five < 3:
                        return False
                    else:
                        five -= 3
        return True

