class BookMyShow:

    def __init__(self, n: int, m: int):
        self.rows = n
        self.seats = m
        self.mydict = {}
        for _ in range(n):
            self.mydict[_] = m

    def gather(self, k: int, maxRow: int):
        x = []
        for _ in range(maxRow+1):
            print(self.mydict[_])
            if self.mydict[_] >= k:
                print("here")
                x = [self.seats-self.mydict[_], _]
                self.mydict[_] -= k
                # return x
                break
        return x

    def scatter(self, k: int, maxRow: int) -> bool:
        for _ in range(maxRow):
            if self.mydict[_] >= k:
                x = [self.seats-self.mydict[_], _]
                self.mydict[_] -= k
                return True
                break
        return False


# Your BookMyShow object will be instantiated and called as such:
obj = BookMyShow(2, 5)
param_1 = obj.gather(4, 0)
param_2 = obj.scatter(5, 1)
print(param_1)
print(param_2)
