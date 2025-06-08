#2D Lists in python 


n = int(input())
m = int(input())

grid = []
for i in range(n):
    # templist = input().split()
    # for j in range(m):
    #     templist[j] = int(templist[j])
    # grid.append(templist)

    grid.append([int(ele) for ele in input().split()])



print(grid)

