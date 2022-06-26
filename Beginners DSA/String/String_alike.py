class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'AaEeIiOoUu'
        len_s = len(s)
        final = [i for i in s[:len_s//2] if i in vowels]
        final_2 = [i for i in s[len_s//2:] if i in vowels]
        if len(final)!= len(final_2):
            return False
        # print(final)
        # print(final_2)
        # final.sort()
        # final_2.sort()
        # for _ in range(len(final)):
        #     if final[_]!=final_2[_]:
        #         return False
        return True
            
        