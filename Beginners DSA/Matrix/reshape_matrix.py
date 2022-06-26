class Solution:
    def matrixReshape(self, mat, r: int, c: int) :
        flatten = [j for i in mat for j in i]
        my_arr = []
        counter = 0
        # print(flatten)
        if len(flatten)!=r*c:
            return mat
        
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(flatten[counter])
                counter += 1
            my_arr.append(temp)
        # print(my_arr)  
        return my_arr