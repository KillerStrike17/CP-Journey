class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(' ')
        my_string = []
        number = []
        for _ in arr:
            my_string.append(_[:-1])
            number.append(int(_[-1]))
        # print(my_string,number)
        xy = zip(my_string, number)
        val = [x for x, _ in sorted(xy, key=lambda p:p[1])]
        # print(val)
        return ' '.join(val)
        # my_string.sort(key = lambd)
