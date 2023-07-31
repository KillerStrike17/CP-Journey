class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minlen = min(len(word1),len(word2))
        maxlen = max(len(word1),len(word2))
        
        lenword1 = len(word1)
        lenword2 = len(word2)
        
        output=""

        for i in range(minlen):
            output += word1[i] + word2[i]
        for j in range(i+1, maxlen):
            if lenword1>lenword2:
                output += word1[j]
            else:
                output += word2[j]
        return output