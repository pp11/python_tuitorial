list=[2,9,1,4,6,7]
def bubble_sorting(list) :
    for i in range (len(list), 0 ,-1):
        for j in range (0, len(list)-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
bubble_sorting(list)

list2=list.copy()
print(list2)
