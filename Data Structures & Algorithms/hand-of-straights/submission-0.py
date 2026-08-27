class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                freq = count[card]

                for next_card in range(card, card + groupSize):
                    if count[next_card] < freq:
                        return False

                    count[next_card] -= freq

        return True