def sort(list):
#outerloop , goes though a range
    for i in range(1, len(list)):
#loop though all the items after 1 , moving lef though the list
        current = list[i]
        position = i
    #doing a comparson between the swapped item
        while position > 0 and list[position-1] > current:
            
            list[position] = list[position-1]
            print(list)
            position -= 1

        list[position] = current

    return list



list = [1,2,3,4,5,6,7,8,9,10]
sort(list)

print(list)