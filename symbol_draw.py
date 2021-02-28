def draw(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end="")
        print()