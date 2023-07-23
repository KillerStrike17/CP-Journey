def reverse(mystr, start, end):
    if start>=end:
        return 
    mystr[start],mystr[end] = mystr[end],mystr[start]
    reverse(mystr, start+1, end-1)


mystr = list("abcde")
reverse(mystr,0,4)
print(mystr)