from grid import Grid
from vec2 import Vec2


def ortho_positions(pos: Vec2, distance=1):
    positions = []
    for j in range(distance + 1):
        ori_pos = pos - Vec2(distance - j, j)
        for i in range((distance - j) * 2 + 1):
            npos = ori_pos + Vec2(i, 0)
            positions.append(npos)
    for j in range(1, distance + 1):
        ori_pos = pos + Vec2(-(distance - j), j)
        for i in range((distance - j) * 2 + 1):
            npos = ori_pos + Vec2(i, 0)
            positions.append(npos)
    return positions


def square_positions(pos: Vec2, distance=1):
    positions = []
    origin = pos - Vec2(distance, distance)
    square_size = distance * 2 + 1
    for j in range(square_size):
        for i in range(square_size):
            npos = origin + Vec2(i, j)
            positions.append(npos)
    return positions


def ortho_neighbor_positions(pos: Vec2, distance=1):
    positions = ortho_positions(pos, distance)
    positions.remove(pos)
    return positions


def square_neighbor_positions(pos: Vec2, distance=1):
    positions = square_positions(pos, distance)
    positions.remove(pos)
    return positions


def ortho_neighbor_positions_in_grid(grid: Grid, pos: Vec2, distance = 1):
    return filter(lambda p: grid.contains(p), ortho_neighbor_positions(pos, distance))


def square_neighbor_positions_in_grid(grid: Grid, pos: Vec2, distance = 1):
    return filter(lambda p: grid.contains(p), square_neighbor_positions(pos, distance))


def ortho_positions_in_grid(grid: Grid, pos: Vec2, distance = 1):
    return filter(lambda p: grid.contains(p), ortho_positions(pos, distance))


def square_positions_in_grid(grid: Grid, pos: Vec2, distance = 1):
    return filter(lambda p: grid.contains(p), square_positions(pos, distance))
