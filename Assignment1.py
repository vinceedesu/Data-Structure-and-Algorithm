#Ladion, Vince Jeremy T.

#creating nested list for each letter
print_L = [[" " for i in range(5)] for j in range(6)]
print_A = [[" " for i in range(5)] for j in range(6)]
print_D = [[" " for i in range(5)] for j in range(6)]
print_I = [[" " for i in range(5)] for j in range(6)]
print_O = [[" " for i in range(5)] for j in range(6)]
print_N = [[" " for i in range(5)] for j in range(6)]


#code for L
for row in range(6):
    for col in range(5):
        if col  == 0 or row == 5:
            print_L[row][col] = "*"

#code for A
for row in range(6):
    for col in range(5):
        if ((col  == 0 or row == 4) and row != 0) or row == 2 or (row == 0 and (col != 0 and col != 4)):
            print_A[row][col] = "*"

#code for D
for row in range(6):
    for col in range(5):
        if ((col  == 0) or (col == 4 and (row != 0 and row != 5)) or ((row == 0 or row == 5) and (col > 0 and col < 3)) ):
            print_D[row][col] = "*"
            
#code for I
for row in range(6):
    for col in range(5):
        if col  == 3 :
            print_L[row][col] = "*"

#code for O
for row in range(6):
    for col in range(5):
        if ((col  == 0 or row == 4) and (col != 0 and col != 4) or (col == 0 or col == 4) and (row != 0 and row != 4)):
            print_O[row][col] = "*"

#code for N
for row in range(6):
    for col in range(5):
        if col  == 0 or col == 4 or row == col:
            print_N[row][col] = "*"
            
for i in range(6):
    for j in range(5):
        print(print_L[i][j], end = " ")
        print(end = " ")
    for j in range(5):
        print(print_A[i][j], end = " ")
        print(end = " ")
    for j in range(5):
        print(print_D[i][j], end = " ")
        print(end = " ")
    for j in range(5):
        print(print_I[i][j], end = " ")
        print(end = " ")
    for j in range(5):
        print(print_O[i][j], end = " ")
        print(end = " ")
    for j in range(5):
        print(print_N[i][j], end = " ")
        print()
