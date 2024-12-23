import random

def rect_with_gap(width, gap_size, height, x_start):
    gap_y_start = random.randint(gap_size+1, height-1)
    up_rect = [(x_start, height), (x_start+width, height), (x_start+width, gap_y_start), (x_start, gap_y_start)]
    down_rect = [(x_start, 0), (x_start+width, 0), (x_start+width, gap_y_start - gap_size), (x_start, gap_y_start - gap_size)]
    return up_rect, down_rect

def generate_rects_with_gap(map_h, map_w, obstacles_count, gap_min_size, gap_max_size, rect_width, space_between, x=0):
    obstacles = []
    cur_x = x+space_between
    
    for _ in range(obstacles_count):
        if cur_x + rect_width+space_between > map_w:
            break
        gap_size = random.randint(gap_min_size, gap_max_size)
        obstacles.extend(rect_with_gap(rect_width, gap_size, map_h, cur_x))
        cur_x += rect_width+space_between
    return obstacles