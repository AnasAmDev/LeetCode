class Solution:
    def isThree(self, n: int) -> bool:
        m = []
        for i in range(1, n+1):
            if n % i == 0:
                m.append(i)
        
        return len(m) == 3