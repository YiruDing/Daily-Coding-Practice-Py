# p3-23

import random

def inputarr(data,size):
    for i in range(size):
        data[i] = random.randint(1,100)
        
def showdata(data,size):
    for i in range(size):
        print('%3d' data[i],end='')
    print()

def quick(d,size,lf,rg):
    if lf<rg:
        lf_idx=lf+1
        while d[lf_idx]<d[lf]:
# If the value of d[lf_idx]<d[lf],and lf_idx+1 is still within the arr...
# Then lf_idx+=1????
            if lf_idx+1 > size:
                break
            lf_idx+=1
        rg_idx=rg
        while d[rg_idx] > d[lf]:
            rg_idx -=1
        while lf_idx<rg_idx:
            d[lf_idx],d[rg_idx]=d[rg_idx],d[lf_idx]
# ???????
            lf_idx+=1
            while d[lf_idx]<d[lf]:
                lf_idx+=1
            rg_idx-=1
            while d[rg_idx]>d[lf]:
                rg_idx-=1
        d[lf],d[rg_idx] = d[rg_idx],d[lf]
        for i in range(size):
            print('%3d' %d[i], end='')
        print()
        
        quick(d,size,lf,rg_idx-1)
        quick(d,size,rg_idx+1,rg)
        
def main():
    data=[0]*100
    size=int(input('Please insert the size of the list(less than 100):'))
    inputarr(data,size)
    print('The orirginal list is:')
    showdata(data,size)
    print('The sorting process is:')
    quick(data,size,0,size-1)
    print('The final result is:')
    showdata(data,size)