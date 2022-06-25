class Solution:
    my_arr = []

    def helper(self, candidates, target, temp_sum, current_sum, index):
        if current_sum > target:
            return
        if index == len(candidates):
            if current_sum == target:
                print("temp_sum", temp_sum)
                self.my_arr.append(temp_sum.copy())
                print("my_arr", self.my_arr)
            return

        current_sum += candidates[index]
        temp_sum.append(candidates[index])
        self.helper(candidates, target, temp_sum, current_sum, index)
        current_sum -= candidates[index]
        temp_sum.pop()

        self.helper(candidates, target, temp_sum, current_sum, index+1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp_sum = []
        index = 0
        current_sum = 0
        # print(candidates)
        self.my_arr = []
        self.helper(candidates, target, temp_sum, current_sum, index)
        return self.my_arr
