import sys


def helper(index, string, n):
    if n < 2:
        return string
    if index >= n//2:
        return string
    else:
        print(index, n-1-index)
        string[index], string[n-1-index] = string[n-1-index], string[index]
        print(string)
        return helper(index+1, string, n)


def reverseString(string):
    # Write your code here.
    return helper(0, list(string), len(string))
    # pass


# t = int(sys.stdin.readline().strip())

# for i in range(t):

string = 'Ui'

for i in (reverseString(string)):
    print(i, end='')

print()
