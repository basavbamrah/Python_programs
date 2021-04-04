'''
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''
m=7  
n=21
a=1
for i in range(m):
    if(i+1 <= (m-1)/2):
        for j in range(i*3,int((n-3)/2)):
            print('-', end="")
        for j in range(1,a+1):
            print(".|.",end="")
        a+=2
        for j in range(i*3,int((n-3)/2)):
            print('-', end="")
    elif(i+1==(m-1)/2+1):
        for i in range(0,int((n-7)/2)):
            print('-',end="")
        print("WELCOME",end="")
        for i in range(0,int((n-7)/2)):
            print('-',end="")
    else:
        a-=2
        for j in range(int((n-3)/2),i*3,1):
            print('-', end="")
        for j in range(a+1,1,-1):
            print(".|.",end="")
        for j in range(int((n-3)/2),i*3,1):
            print('-', end="")
    print()
