# p4-4

import random

val=0
data=[0]*80
for i in range(80):
    data[i] = random.randint(1,150)
while val != -1:
    find=0
    val=int(input('Please insert the value(1-150),insert "-1" to exit:'))
    for i in range(80):
        if data[i]==val:
            print('Found the value [%3d] in index %3d' %(data[i],i))
            find+=1
    if find==0 and val !=-1:
        print('##### Couldn\'t find the value [%3d] ##### ' %val)
print('The list:')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]  ' %(i*8+j+1),data[i*8+j],end='')
    print('')