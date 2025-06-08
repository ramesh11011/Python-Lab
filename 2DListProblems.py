# Trace or the diagonal of the matrix

n = int(input())
grid = []

for i in range(n):
    grid.append([int(ele) for ele in input().split()])

trace = []
for i in range(n):
    templist = grid[i][i]
    trace.append(templist)
    
print(trace)