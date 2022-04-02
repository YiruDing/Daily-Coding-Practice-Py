# 4-8

import random

def interpolation_search(data,val):
    low=0
    high=49
    print('We Are Searching...')
    while low<= high and val !=-1:
        mid=low+int((val-data[low])*(high-low)/(data[high]-data[low]))
        if val==data[mid]:
            return mid
        elif val< data[mid]:
            print('%d is between %d[%3d] and the midian %d[%3d], look for the left' %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val>data[mid]:
            print('%d is between %d[%3d] and the midian %d[%3d], look for the right' %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
    return -1

val=1
data=[0]*50
for i in range(50):
    data[i]=val
    val=val+random.randint(1,5)
    
while True:
    num=0
    val=int(print('Please insert the value(1-150), insert-1 to exit: '))
    if val==-1:
        break
    num=interpolation_search(data,val)
    if num==-1:
        print('##### Sorry!We didn\'t find [%3d] #####' %val) 
    else:
        print('Found [%3d] in index %2d' %(data[num],num+1))
print('The content of the data:')
for i in range(5):
    for j in range(10):
        print('%3d-%-3d' %(i*10+j+1,data[i*10+j]),end='')
        print()