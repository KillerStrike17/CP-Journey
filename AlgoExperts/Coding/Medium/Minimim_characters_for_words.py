from collections import Counter
def minimumCharactersForWords(words):
    # Write your code here.
    if words:
        main_temp = Counter(words[0])
        for _ in words[1:]:
            temp = Counter(_)
            
            for key in temp:
                if key in main_temp:
                    if main_temp[key] < temp[key]:
                        main_temp[key] = temp[key]
    
    
                else:
                    main_temp[key] = temp[key]
        print(main_temp)
        output_arr = []
        for key in main_temp:
            temp = [key]*main_temp[key]
            output_arr += temp
        return output_arr
    else:
        return []