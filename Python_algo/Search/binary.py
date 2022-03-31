# p4-5

import random

def bin_search(data,val):
    low=0
    high=49
    while low <=high and val !=-1:
        mid=int((low+high)/2)
        if val<data[mid]:
            print('%d is located between index %d[%3d] and median %d[%3d], go for the left part.' %(val,low,data[low],mid,data[mid]))
            high=mid-1
        elif val>data[mid]:
            print('%d is located between index %d[%3d] and median %d[%3d], go for the right part.' %(val,high,data[high],mid,data[mid]))
            low=mid+1
        else:
            return mid
    return -1

val=1
data=[0]*50
for i in range(50):
    data[i]=val
    val=val+random.randint(1,5)
    
while True:
    num=0
    val=int(input('Please insert the value(1-150),insert -1 to exit:'))
    if val ==-1:
        break
    num=bin_search(data,val)
    # 3/30 ???
    if num==-1:
        print('[%3d] is not found' %val)
    else:
        print('[%3d] is found in index %2d' %(data[num],num))
        
    print('The content of the data:')
    for i in range(5):
        for j in range(10):
            print('%3d-%-3d' %(i*10+j+1,data[i*10+j]),end='')
    print()