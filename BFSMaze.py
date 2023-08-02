def BFSMaze(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(x, y):
        if (x, y) == tuple(destination):
            return True

        if (x, y) in visited:
            return False

        visited.add((x, y))

        # Move in four directions: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            new_x, new_y = x, y
            while 0 <= new_x + dx < rows and 0 <= new_y + dy < cols and maze[new_x + dx][new_y + dy] == 0:
                new_x += dx
                new_y += dy
            if dfs(new_x, new_y):
                return True

        return False

    return dfs(start[0], start[1])


# Test data
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]

print(BFSMaze(maze, start, destination))  # Output: True
