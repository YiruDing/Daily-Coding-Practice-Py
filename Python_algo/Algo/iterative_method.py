# P1-19

# for loop
sum = 1
n=int(input('Please insert n='))
for i in range(0,n+1):
    for j in range(i,0,-1):
        sum *= j
    print('%d!=%3d' %(i,sum))
    sum = 1
    
# while loop
i=1
while i < 10:
    print(i)
    i += 1