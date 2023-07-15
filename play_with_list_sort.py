num_list = [5,4,3,2,4]
for i, num in enumerate(num_list[:-1]):
    if (num<num_list[i+1]):
        print(i+1)
