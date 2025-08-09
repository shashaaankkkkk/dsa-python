class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.result = []
        total = 0
        for num in nums:
            total += num
            self.result.append(total)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.result[right]
        else:
            return self.result[right] - self.result[left - 1]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)

    queries = [(0, 2), (2, 5), (0, 5)]
    for left, right in queries:
        print(f"sumRange({left}, {right}) = {obj.sumRange(left, right)}")

