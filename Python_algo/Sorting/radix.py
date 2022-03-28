# p3-27

import random

def inputarr(data,size):
    for i in range(size):
        data[i]=random.randint(0,999)
        
def showdata(data,size):
    for i in range(size):
        print('%3d' %data[i], end='')
    print()
    
def radix(data,size):
    n=1
    while n<=100:
        tmp=[[0]*100 for row in range(10)]
        for i in range(size):
            m=(data//n)%10
            tmp[m][i] = data[i]
        k=0
        for i in range(10):
            for j in range(size):
                if tmp[i][j]!=0:
                    data[k]=tmp[i][j]
                    # store the value of tmp[i][j] in data[k]
                    k+=1
        print('After ％3d digits sorting:' %n,end='')
        showdata(data,size)
        n=10*n
        
def main():
    data=[0]*100
    size=int(input('Please insert the size of the list(less than 100):'))
    print('The original list is:')
    inputarr(data,size)
    showdata(data,size)
    radix(data,size)

main()