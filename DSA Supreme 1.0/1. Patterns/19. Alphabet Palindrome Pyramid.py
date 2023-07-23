import string

mystrings = list(string.ascii_uppercase)
print("Enter Length of Full Pyramid:")
pyramidLength = int(input())
for i in range(pyramidLength):
    output_half = ' '.join(mystrings[:i+1])
    print(output_half+output_half[:-1][::-1])

