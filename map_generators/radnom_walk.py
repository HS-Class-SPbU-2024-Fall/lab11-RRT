import random


def generate_random_walk_map(map_width, map_height, fill_terrain, walk_terrain, number_of_paths, max_path_len):
    if map_height < 10 or map_width < 10:
        raise ValueError("Map height and width must be greater than 10")
    
    map = [[fill_terrain for _ in range(map_width)] for _ in range(map_height)]
    starting_point = (map_width // 2, map_height // 2)
    current_position = starting_point

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(number_of_paths):
        random_directions = random.sample(directions, 2)
        for _ in range(max_path_len):
            if random.randint(0, 100) > 85:
                random_directions = random.sample(directions, 3)
            
            x, y = current_position
            map[y][x] = walk_terrain

            neighbors = []
            for dx, dy in random_directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < map_width and 0 <= ny < map_height:
                    neighbors.append([nx, ny])

            if neighbors:
                current_position = random.choice(neighbors)

                if not (2 < current_position[0] < map_width-5 and 2 < current_position[1] < map_height-5):
                    current_position = starting_point
                    break
                
    for _ in range(8):
        for y in range(map_height):
            for x in range(map_width):
                delta = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                window_sum = 0
                walls_sum = 0
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < map_width and 0 <= ny < map_height:
                        window_sum += 1
                        if map[ny][nx] == fill_terrain:
                            walls_sum += 1
                if window_sum > 0 and walls_sum / window_sum < 0.5:
                    map[y][x] = walk_terrain
    
    return map