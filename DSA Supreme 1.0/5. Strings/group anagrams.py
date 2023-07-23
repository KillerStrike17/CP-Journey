from collections import defaultdict
mystr = ["eat","tea","tan","ate","nat","bat"]

mydict = defaultdict(lambda :[])

for _ in mystr:
    mydict["".join(sorted(_))].append(_)

print(list(mydict.values()))