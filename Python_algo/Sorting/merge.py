# p3-18

from email.mime import base


list1=[20,45,51,88,99999]
list2=[98,10,23,15,99999]
list3=[]

def merge_sort():
    global list1
    global list2
    global list3
    
    select_sort(list1, len(list1)-1)
    select_sort(list2, len(list2)-1)
    
    print('\n the result of list1: ', end='')
    for i in range(len(list1)-1):
        print(list1[i], ' ', end = '')
        
    print('\n the result of list2: ', end='')
    for i in range(len(list2)-1):
        print(list1[i], ' ', end = '')
    print()
    
    for i in range(60):
        print('=',end='')
    print()
    
    print('\n The result of merge sort:', end='')
    for i in range(len(list1)+len(list2)-2):
        print('%d ' %list3[i], end='')

def select_sort(data,size):
    for base in range(size-1):
        small = base
        for j in range(base+1, size):
            if data[j] < data[small]:
                small = j    
        data[small], data[base] = data[base], data[small]
        
def My_Merge(size1,size2):
    global list1
    global list2
    global list3
    
    index1 = 0
    index2 = 0
    for index3 in range(len(list1)+len(list2)-2):
        if list1[index1] < list2[index2]:
            list3.append(list1[index1])
            index1+=1
            print('This number %d is from list1' %list3[index3])
        else:
            list3.append(list2[index2])
            index2+=1
            print('This number %d is from list2' %list3[index3])
        print('The merged result so far: ', end='')
        for i in range(index3+1):
            print(index3[i], ' ', end='')
        print('\n')
        
merge_sort()
            