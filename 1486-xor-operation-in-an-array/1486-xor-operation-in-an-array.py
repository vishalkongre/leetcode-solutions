class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        result = 0
        for i in range(n):
            nums.insert(i, start + 2*i)
        for num in nums:
            result ^=num

        return result


        