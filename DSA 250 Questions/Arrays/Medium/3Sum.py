class Solution:
    def threeSum(self, nums):
        len_nums = len(nums)
        if len_nums>2:
            output_arr = {}
            for _ in range(len_nums):
                first_val = nums[_]
                temp_list = nums[_+1:]
                # print(first_val,temp_list)
                for i in range(len(temp_list)):
                    second_val = temp_list[i]
                    temp_list_3 = temp_list[i+1:]
                    check_val = 0-first_val-second_val
                    # print(second_val,temp_list_3)
                    if check_val in temp_list_3:
                        temp = [first_val, second_val, check_val]
                        temp.sort()
                        output_arr[tuple(temp)] = 1
                        # break
            return output_arr.keys()
        else:
            return []