"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique
"""

class Solution:
    def canCompleteCircuit(self, gas, cost):

        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):

            diff = gas[i] - cost[i]

            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1

        return start