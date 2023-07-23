class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i = 0
        row = 0
        direction = True
        output = [[] for _ in range(numRows)]
        print(output)
        while True:
            if direction:
                while(row<numRows and i<len(s)):
                    output[row].append(s[i])
                    row +=1
                    i+=1
                row = numRows - 2
            else:
                while(row>=0 and i<len(s)):
                    output[row].append(s[i])
                    row -=1
                    i+=1
                row = 1
            if i>=len(s):
                break
            direction = not direction
        # print(output)
        return "".join(["".join(x) for x in output])