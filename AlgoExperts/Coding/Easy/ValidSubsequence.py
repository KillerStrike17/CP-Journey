from collections import Counter


def isValidSubsequence(array, sequence):
    counter = 0
    val = False
    for _ in array:
        if _ == sequence[counter]:
            counter += 1
        if counter == len(sequence):
            val = True
            break
    return val
