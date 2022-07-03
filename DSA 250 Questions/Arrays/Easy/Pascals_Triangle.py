class Solution:
    def generate(self, numRows: int):
        if numRows>0:
            output_array = [[1]]
            for _ in range(1,numRows):
                temp_arr = []
                for i in range(_+1):
                    if i ==0 or i==_:
                        temp_arr.append(1)
                    else:
                        temp_arr.append(output_array[_-1][i] + output_array[_-1][i-1])
                output_array.append(temp_arr)
                        
        return output_array
        