from math import gcd 

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        count = 0

        for i in range(1, int(g ** 0.5) + 1):
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            
        return count