a =[1,2,3,4,5,6,7]
sum_val = 9

for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i]+a[j]+a[k] ==sum_val:
                print(a[i],a[j],a[k])
