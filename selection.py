#creating my function to sort 
def sort(list):
    #first loop is used to find what should be the mininum
    for i in range(9):
        minpos = i
        #second loop is reduce the unsoreted list 
        for j in range(i,10):
            if list[j] < list[minpos]:
                minpos =j
        #below I am swaping the numbers in my loop 
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp



list = [1,2,3,46,5,6,7,80,9,10]
sort(list)

print(list)