class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = self.add_str(num1, len(num1)-1, num2, len(num2)-1,0)
        return ans[::-1]

    def add_str(self,num1, index1, num2, index2, carry):
        if index1<0 and index2<0:
            if carry!=0:
                return chr(carry + ord("0"))
            else:
                return ""

        if index1<0:
            temp1 = 0
        else:
            temp1 = ord(num1[index1])-ord("0")
        if index2<0:
            temp2 =0
        else:
            temp2 = ord(num2[index2])-ord("0")
        # print(temp1,num1)
        # print(temp2,num2)
        tempsum = temp1 + temp2 +carry
        carry = tempsum //10
        digit = tempsum%10
        ans = chr(digit + ord("0"))
        # print(digit, carry, tempsum,ans)
        ans += self.add_str(num1, index1-1, num2, index2-1, carry)
        return ans