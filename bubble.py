def sort(num):
    for i in range (len(list) -1,0,-1):
        for j in range(i):
            if list[j]> list[j+1]:
                temp= list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                

list = [1,2,3,4,5,6,7,8,9,10]
sort(list)

print(list)