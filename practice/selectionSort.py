def search(list):
    for i in range(5):
        minpos = i
        for j in range(i, 5):
            if list[minpos]>list[j]:
                minpos=j

        temp=list[i]
        list[i]=list[minpos]
        list[minpos] = temp

        print(list)

list=[6,7,3,2,9]
print(search(list))

print(list)