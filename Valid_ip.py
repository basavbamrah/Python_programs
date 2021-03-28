# BY: BASAV BAMRAH
# print total possible valid ip adddress
# 28.03.2021 

def check(ip):
    """checks if the passed argument is a valid ip or not

    Args:
        ip ([string])
    Returns:
        [boolean]
    """
    ip =ip.split(".")
    for i in ip:
        if(int(i)==0 and len(i)>1):
            return False
        elif(int(i)>255 ):
            return False
        elif(i[0]=='0' and int(i)>0):
            return False
    
    return True

def calc(n):
    vip=[]
    temp= n
    l=len(n)
    if(l<4 or l>12):
        print("INVALID INPUT\n")
        exit(0)
    else:
        for i in range(1,l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    temp=temp[:k]+'.'+temp[k:]
                    temp=temp[:j]+'.'+temp[j:]
                    temp=temp[:i]+'.'+temp[i:]
                    if check(temp):
                        vip.append(temp)
                    temp=n
    
    print(vip)



if __name__ =="__main__":
    n=input("Enter an ip:\n")
    calc(n)