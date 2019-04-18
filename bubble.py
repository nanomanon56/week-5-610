def sort(list):
    for i in range (len(list) -1,0,-1):
        for j in range(i):
            if list[j]> list[j+1]:
                temp= list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                

list = [99,1,2,3,88,4,5,6,765,7,8,9,10]
sort(list)

print(list)