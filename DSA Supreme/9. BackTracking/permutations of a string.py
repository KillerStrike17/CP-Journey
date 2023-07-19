input_str = list("abc")

def permutation(input_str,i):
    if i>=len(input_str):
        print("".join(input_str))
        # print(input_str)
        return
    
    for j in range(i, len(input_str)):
        input_str[i],input_str[j] = input_str[j],input_str[i]
        permutation(input_str,i+1)
        input_str[i],input_str[j] = input_str[j],input_str[i]

print(permutation(input_str,0))