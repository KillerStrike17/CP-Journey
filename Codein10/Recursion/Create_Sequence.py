output_arr = []


def helper(n, temp_ans):
    # print("temp_ans:", temp_ans)
    if temp_ans:
        if int(temp_ans) > n:
            return
        else:
            output_arr.append(int(temp_ans))

    temp_ans += '2'
    helper(n, temp_ans)
    temp_ans = temp_ans[:-1]

    temp_ans += '5'
    helper(n, temp_ans)
    temp_ans = temp_ans[:-1]


def createSequence(n):
    global output_arr
    output_arr = []
    helper(n, '')
    output_arr.sort()
    return output_arr

    # Write your code here.


createSequence(60)
