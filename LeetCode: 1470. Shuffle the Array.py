class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            # Appending the i-th element from the first half
            result.append(nums[i])
            # Appending the i-th element from the second half
            result.append(nums[i+n])
        return result

