def substring(index, mystr, output_str,n,output_arr):
    if index ==n:
        print(output_str)
        output_arr.append(output_str)
        return 
    #Exclude
    substring(index+1, mystr, output_str,n,output_arr)

    #Include
    output_str +=mystr[index]
    substring(index+1, mystr, output_str,n,output_arr)


output_arr = []
print(substring(0, "abcde", "",5,output_arr))
print(output_arr,len(output_arr))
output_arr.sort(key=len)
print(output_arr,len(output_arr))
