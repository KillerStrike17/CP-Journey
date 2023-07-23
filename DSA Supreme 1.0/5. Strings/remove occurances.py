s = "daabcbaabcbc"
part = "abc"

pos = s.find(part)
print(pos)
while pos>0:
    s = s.replace(part,"")
    print("S",s)
    pos = s.find(part)
print(s)