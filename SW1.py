
print_L = [[" " for i in range (6)] for j in range (6)]
print_A = [[" " for i in range (6)] for j in range (6)]
print_D = [[" " for i in range (6)] for j in range (6)]
print_I = [[" " for i in range (6)] for j in range (6)]
print_O = [[" " for i in range (6)] for j in range (6)]
print_N = [[" " for i in range (6)] for j in range (6)]

for row in range (6): 
    for col in range (6):
        if  col == 0  or row == 5:
            print_L[row][col] = "*"
            
for row in range(6):
    for col in range(6):
        if ((col  == 0 or row == 4) and row != 0) or row == 2 or (row == 0 and (col != 0 and col != 4)):
            print_A[row][col] = "*"

for row in range (6): 
    for col in range (6):
        if  ((row == 0 or row == 5) and  col!=5) or ((col == 0 or col == 5) and (row!=0 and row!=5 )):
            print_D[row][col] = "*"

for row in range (6): 
    for col in range (6):
        if  col == 2  or row == 5 or row == 0 or col == 3:
            print_I[row][col] = "*"

for row in range (6): 
    for col in range (6):
        if  ((row == 0 or row == 5) and (col!=0 and col!=5)) or ((col == 0 or col == 5) and (row!=0 and row!=5 )):
            print_O[row][col] = "*"
            
for row in range (6): 
    for col in range (6):
        if  col == 0  or col == 5 or row == col:
            print_N[row][col] = "*"

for i in range(6):
    for j in range(6):
        print(print_L[i][j], end=" ")
    # for j in range(6):
    #     print(print_A[i][j], end=" ")
    for j in range(6):
        print(print_D[i][j], end=" ")
    for j in range(6):
        print(print_I[i][j], end=" ")
    for j in range(6):
        print(print_O[i][j], end=" ")
    for j in range(6):
        print(print_N[i][j], end=" ")
    print()