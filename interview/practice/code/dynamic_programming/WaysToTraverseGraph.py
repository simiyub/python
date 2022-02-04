def ways_to_traverse_graph(width, height):
    ways = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

    for width_index in range(1, width + 1):
        for height_index in range(1, height + 1):
            if width_index == 1 or height_index == 1:
                ways[height_index][width_index] = 1
            else:
                ways_left = ways[height_index][width_index - 1]
                ways_top = ways[height_index - 1][width_index]
                ways[height_index][width_index] = ways_left + ways_top
    return ways[height][width]