"""
846. Hand of Straights
Alice has a hand of cards, given as an array of integers.
Now she wants to rearrange the cards into groups so that each group is size groupSize, and consists of groupSize consecutive cards.
Return true if and only if she can.
"""

from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):

        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in sorted(hand):

            if count[num] > 0:

                for i in range(groupSize):

                    if count[num + i] == 0:
                        return False

                    count[num + i] -= 1

        return True