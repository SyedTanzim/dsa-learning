class NumArray:

    def __init__(self, nums: list[int]):
        self.data = nums

    def sumRange(self, left: int, right: int) -> int:
        right = right
        left = left
        sum = 0

        for i in range(left, right+1):
            sum += self.data[i]
        
        return sum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)