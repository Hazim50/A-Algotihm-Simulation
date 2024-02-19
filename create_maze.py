import random
def create_maze(maze_size,road_ratio):
    maze = [[random.choices([0, 1], weights=[road_ratio, 1-road_ratio])[0] for _ in range(maze_size[1])] for _ in range(maze_size[0])]
    return maze