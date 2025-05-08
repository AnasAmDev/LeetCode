from itertools import accumulate
from typing import List

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        running_totals = accumulate(nums)
        zero_count = sum(total == 0 for total in running_totals)
        return zero_count
