## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
my_dict = {}

def fib(n):
    global my_dict
    if n==0 or n==1:
        return n
    if n in my_dict:
        return my_dict[n]
    val = fib(n-1) + fib(n-2)
    my_dict[n]=val
    return val
print(fib(n))


# Or


my_dict[0] = 0
my_dict[1] = 1
def fib(n):
    for _ in range(2, n+1):
        my_dict[_] = my_dict[_-1] + my_dict[_-2]
        
    return my_dict[n]




#Or


prev_1 = 0
prev_2 = 1   
curr = prev_1 + prev_2
def fib(n):
    global prev_1, prev_2,curr
    for _ in range(2, n+1):
        curr = prev_1 + prev_2
        prev_1 = prev_2
        prev_2 = curr
        
    return curr
    