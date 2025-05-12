class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def compute_gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        min_number = min(nums)
        max_number = max(nums)
        return compute_gcd(min_number, max_number) 