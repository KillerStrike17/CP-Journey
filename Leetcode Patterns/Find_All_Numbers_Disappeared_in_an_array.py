class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # nums.sort()
        my_dict = Counter(nums)
        a = []
        for _ in range(1, n+1):
            if _ not in my_dict:
                a.append(_)
        return a
