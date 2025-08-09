# pivot_index.py

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum = 0
        total = sum(nums)
        for i in range(len(nums)):
            rightsum = total - nums[i] - leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
        return -1


if __name__ == "__main__":
    # Example usage
    nums = [1, 7, 3, 6, 5, 6]
    obj = Solution()
    result = obj.pivotIndex(nums)
    print("Pivot Index:", result)

