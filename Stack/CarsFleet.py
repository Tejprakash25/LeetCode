class Solution(object):
    def carFleet(self, target, position, speed):
        fleets = 0
        last = 0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = float(target - p) / s
            if t > last:
                fleets += 1
                last = t
        return fleets