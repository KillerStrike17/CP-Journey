'''

	Time complexity: O(4 ^ N / sqrt(N))
	Space complexity: O(4 ^ N / sqrt(N))

	where N is the given number

'''


def printParenthesesHelper(cur, opn, close, mx):

    if len(cur) == (mx * 2):

        print(cur)
        return

    if opn < mx:

        printParenthesesHelper(cur + '{', opn+1, close, mx)

    if close < opn:

        printParenthesesHelper(cur + '}', opn, close + 1, mx)


def printParantheses(n):

    strr = ""
    printParenthesesHelper(strr, 0, 0, n)
