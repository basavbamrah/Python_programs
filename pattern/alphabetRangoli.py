"""

----c----           
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


#size 5

--------e--------       
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""


def print_rangoli(size):
    ch = chr(size + 97 - 1)
    n = size * 3 + size - 3
    a = int(n / 2)
    y = 1
    lh = 1
    for i in range(2 * size - 1):
        if i < size:
            for j in range(a):
                print("-", end="")
            ch = chr(size + 97 - 1)
            for j in range(i + 1):
                if i == 0:
                    print(ch, end="")
                else:
                    print(ch, end="-")
                x = ord(ch)
                x -= 1
                ch = chr(x)
            if i >= 1:
                x+=2
                ch=chr(x)
                for j in range(i):
                    if j < i - 1:
                        print(ch, end="-")
                    else:
                        print(ch, end="")
                    x = ord(ch)
                    x += 1
                    ch = chr(x)
            for j in range(a):
                print("-", end="")
        else:
            for j in range(1, y * 2 + 1):
                print("-", end="")
            
            ch = chr(size + 97 - 1)
            for j in range(size - lh):
                if i == 2 * size - 1-1:
                    print(ch,end="")
                else:
                    print(ch, end="-")
                x = ord(ch)
                x -= 1
                ch = chr(x)
            x+=2
            ch=chr(x)
            for j in range(size - lh-1):
                if(j==size-lh-1-1):
                    print(ch,end="")
                else:
                    print(ch, end="-")
                    x = ord(ch)
                    x += 1
                    ch = chr(x)
                    
            for i in range(1, y * 2 + 1):
                print("-", end="")
            lh += 1
            y += 1
        a -= 2
        print()




if __name__ == "__main__":
    n = int(input("Enter a number between 3 and 26\n"))
    print_rangoli(n)
