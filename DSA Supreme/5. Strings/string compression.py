class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        count = 1
        prev =chars[0]
        for i in range(1,len(chars)):
            if chars[i] == prev:
                count+=1
            else:
                chars[index] = prev
                index = index +1
                if count>1:
                    start = index
                    while count>0:
                        chars[index] = str(count%10)
                        count= count//10
                        index = index +1
                    end = index
                    # print(chars[start:end+1])
                    chars[start:end] = chars[start:end][::-1]
                    # print(chars[start:end+1])
                count = 1
                prev = chars[i]
        chars[index] = prev
        index +=1
        if count>1:
            start = index
            
            while count>0:
                chars[index] = str(count%10)
                count= count//10
                index = index +1
            end = index
            # print(chars[start:end])
            chars[start:end] = chars[start:end][::-1]
            # print(chars[start:end])
        return index