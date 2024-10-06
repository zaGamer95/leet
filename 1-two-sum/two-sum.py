class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # simple O(n^2) solution
        answer = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    answer.append(i)
                    answer.append(j)
                    break
        """
        # faster solution using hash map O(n) complexity
        n = len(nums)
        hash_map = dict()
        for i in range(0, n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i

        return answer