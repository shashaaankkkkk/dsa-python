class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            right_sum=total-leftsum-nums[i]

            if right_sum==leftsum:
                return i
            leftsum+=nums[i]
        return -1

if __name__ == "__main__":
    obj=Solution()
    inums = [1, 7, 3, 6, 5, 6]
    a=obj.findMiddleIndex(inums)
    print("middle index is",a)
