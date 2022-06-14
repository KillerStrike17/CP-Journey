def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    sum_val = []
    for _ in range(len(queries[:-1])):
        sum_val.append(sum(queries[:_+1]))
    return sum(sum_val)
    # return 0
