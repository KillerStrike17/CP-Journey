input_string = input()

input_string = list(input_string)
for _ in range(len(input_string)):
    if input_string[_]== " ":
        input_string[_]="@"
        
print("".join(input_string))