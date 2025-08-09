class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum=0
        result=[]
        for i in nums:
            sum+=i
            result+=[sum]

        return result


if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()

    # Example test cases
    nums = [1, 2, 3, 4]
    print(f"Running sum of {nums}: {solution.runningSum(nums)}")

    nums2 = [1, 1, 1, 1, 1]
    print(f"Running sum of {nums2}: {solution.runningSum(nums2)}")

    nums3 = [3, 1, 2, 10, 1]
    print(f"Running sum of {nums3}: {solution.runningSum(nums3)}")
