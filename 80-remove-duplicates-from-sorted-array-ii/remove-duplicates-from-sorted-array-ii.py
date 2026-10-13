class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        index = 1
        freq = 1
        count = 1
        last = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != last and freq < 2:
                nums[index] = nums[i]
                count += 1
                last = nums[i]
                index += 1
            
            elif nums[i] == last and freq < 2:
                nums[index] = nums[i]
                freq += 1
                count += 1
                index += 1
            
            elif nums[i] != last and freq >= 2:
                nums[index] = nums[i]
                last = nums[i]
                freq = 1
                count += 1
                index += 1

            elif nums[i] == last and freq >= 2:
                continue
        
        return count
            
            
        