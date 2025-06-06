import random

from grid import Grid
from neighborhood import ortho_positions_in_grid, square_positions_in_grid
from vec2 import Vec2

#
def random_positions(grid: Grid, n: int):
    square_positions = []
    square_indexes = list(range(grid.width * grid.height))
    assert n <= len(square_indexes)
    for i in range(n):
        sq_index = random.choice(square_indexes)
        sq_pos = grid.index_to_pos(sq_index)
        area_positions = square_positions_in_grid(grid, sq_pos, 1)
        for pos in area_positions:
            idx = grid.pos_to_index(pos)
            if idx in square_indexes:
                square_indexes.remove(idx)
        square_positions.append(sq_pos)
    return square_positions

if __name__ == "__main__":
    rng_seed = random.randint(0, 100)
    print(f"seed: {rng_seed}")
    random.seed(rng_seed)
    #-----
    grid = Grid(Vec2(10, 10), "[ ]")
    nb_root_obstacles = 12
    positions = random_positions(grid, nb_root_obstacles)
    print(f"{positions}")
    for pos in positions:
        grid[pos] = "[#]"
    print(f"{grid}")
