haystack = "saadbutsad"
needle = "sad"

if needle in haystack:
    print(haystack.index(needle))
else:
    print("-1")

needle_length = len(needle)
for _ in range(len(haystack)-needle_length):
    if haystack[_:_+needle_length] == needle:
        print(_)
        break

print(-1)
    