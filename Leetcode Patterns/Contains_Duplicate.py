class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val = False
        my_dict = {}
        for _ in nums:
            # print(_,my_dict.keys())
            if _ in my_dict.keys():
                # print("here")
                val = True
                break
            else:
                my_dict[_] = 1
        return val
