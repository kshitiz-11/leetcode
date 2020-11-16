import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        even_count = 0

        for num in nums:
            val = int(math.log10(num)) + 1
            # print(val)
            if val % 2 == 0:
                even_count += 1

            else:
                continue

        return even_count