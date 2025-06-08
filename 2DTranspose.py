# Transpose of the matrix

number = int(input())
grid = []
for i in range(number):
    grid.append([int(ele) for ele in input().split()])

for i in range(number):
    for j in range(number):
        if(j>i):
            templist = grid[j][i]
            grid[j][i] = grid[i][j]
            grid[i][j] = templist

for i in range(number):
    print(grid[i])