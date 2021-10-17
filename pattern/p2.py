"""
5 4 3 2 1 1 2 3 4 5 

5 4 3 2     2 3 4 5 

5 4 3         3 4 5 

5 4             4 5 

5                 5 

"""

row = 6
for i in range(0, row):
    for j in range(row - 1, i, -1):
        print(j, "", end="")
    for l in range(i):
        print("    ", end="")
    for k in range(i + 1, row):
        print(k, "", end="")

    print("\n")
