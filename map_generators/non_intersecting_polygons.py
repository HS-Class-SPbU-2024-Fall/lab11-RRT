import math
import random
from shapely.geometry import Polygon as ShapelyPolygon, Point

def generate_random_point(width, height):
    return (random.uniform(0, width), random.uniform(0, height))

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def angle_from_horizontal(p1, p2):
    return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points):
    points = sorted(points)
    lower = []
    for point in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]

def generate_random_polygon(width, height, max_vertices, max_distance):
    num_vertices = random.randint(3, max_vertices)
    points = []
    
    points.append(generate_random_point(width, height))
    
    for _ in range(1, num_vertices):
        while True:
            new_point = generate_random_point(width, height)
            if distance(new_point, points[-1]) <= max_distance:
                points.append(new_point)
                break
    return graham_scan(points)

def is_intersecting(polygon, existing_polygons):
    shapely_polygon = ShapelyPolygon(polygon)
    for existing in existing_polygons:
        shapely_existing = ShapelyPolygon(existing)
        if shapely_polygon.intersects(shapely_existing):
            return True
    return False

def generate_non_intersecting_polygons(number_of_polygons: int, width: int, height: int, max_vertices: int, max_distance: float):
    polygons = []
    while len(polygons) < number_of_polygons:
        polygon = generate_random_polygon(width, height, max_vertices, max_distance)
        if not is_intersecting(polygon, polygons):
            polygons.append(polygon)
    return polygons