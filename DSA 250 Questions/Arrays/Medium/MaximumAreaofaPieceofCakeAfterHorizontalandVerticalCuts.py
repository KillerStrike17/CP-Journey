class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        verticalCuts.sort()
        horizontalCuts.sort()
        diff_h = []
        len_h = len(horizontalCuts)
        for _ in range(len_h):
            if _==0:
                diff_h.append(horizontalCuts[_]-0)
            # elif _ ==len_h:
            #     diff_h.append(w+1-horizontalCuts[_])
            else:
                diff_h.append(horizontalCuts[_]-horizontalCuts[_-1])
        diff_h.append(h-horizontalCuts[len_h-1])
        print(diff_h)
        diff_v = []
        len_v = len(verticalCuts)
        for _ in range(len_v):
            if _==0:
                diff_v.append(verticalCuts[_]-0)
            # elif _ ==len_h:
            #     diff_h.append(w+1-horizontalCuts[_])
            else:
                diff_v.append(verticalCuts[_]-verticalCuts[_-1])
        diff_v.append(w-verticalCuts[len_v-1])
        print(diff_v)
        return int((max(diff_v)*max(diff_h))%(10**9 +7))