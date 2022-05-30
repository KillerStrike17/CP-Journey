def tournamentWinner(competitions, results):
    # Write your code here.
    my_dict = {}
    for _ in range(len(competitions)):
        if results[_] == 0:
            if competitions[_][1] in my_dict.keys():
                my_dict[competitions[_][1]] += 1
            else:
                my_dict[competitions[_][1]] = 1
        else:
            if competitions[_][0] in my_dict.keys():
                my_dict[competitions[_][0]] += 1
            else:
                my_dict[competitions[_][0]] = 1
    return max(my_dict, key=lambda x: my_dict[x])

    # return ""
