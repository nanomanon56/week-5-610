import random

list=  [7,89,1,99,3487]


print(list)
 
num_city = {7:"Boston", 89:"New York",1:"Austin",99:"Tampa",3487:"Burlington" }
 
if random.choice(list) == 7:
     print(num_city)
else:
    print("you get nothing")