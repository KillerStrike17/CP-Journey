from sys import stdin, stdout, setrecursionlimit
setrecursionlimit(10 ** 7)


def helper(arr, req_sum, K, index, bucket_num, bucket_sum, already_picked):
    if bucket_num == K+1:
        return True
    if bucket_sum == req_sum:
        return helper(arr, req_sum, K, 0, bucket_num+1, 0, already_picked)
    if bucket_sum > req_sum:
        return False
    if index == len(arr):
        return False
    if already_picked[index] == 1:
        return helper(arr, req_sum, K, index+1, bucket_num, bucket_sum, already_picked)
    else:
        already_picked[index] = 1
        bucket_sum += arr[index]
        val = helper(arr,  req_sum, K, index+1, bucket_num,
                     bucket_sum, already_picked)
        already_picked[index] = 0
        bucket_sum -= arr[index]

        val2 = helper(arr,  req_sum, K, index+1, bucket_num,
                      bucket_sum, already_picked)

        return val or val2


def canPartitionKSubsets(arr, n, K):
    # Write your code here.
    already_picked = [0]*n
    req_sum = sum(arr)
    if req_sum % K != 0:
        return False
    req_sum = req_sum//K
    return helper(arr, req_sum, K, 0, 1, 0, already_picked)
    pass

# # Taking input using fast I/0.
# def takeInput():
#     N = int(stdin.readline())
#     arr = list(map(int, stdin.readline().strip().split(" ")))
#     K = int(stdin.readline())
#     return N, arr, K

# # Main.
# tc = int(input())
# while tc > 0:
#     N, arr, K = takeInput()
#     ans = canPartitionKSubsets(arr, N, K)
#     stdout.write(str(ans) + "\n")
#     tc -= 1


print(canPartitionKSubsets([4, 3, 1, 3, 4, 1, 2], 8, 3))
