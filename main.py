import random

from grid import Grid
from vec2 import Vec2

if __name__ == "__main__":
    grid = Grid(Vec2(12, 6), ".")
    rng_seed = random.randint(0, 100)
    print(f"seed: {rng_seed}")
    random.seed(rng_seed)
    indexes = sorted(random.choices(range(grid.width * grid.height), k=10))
    print(indexes)
    for index in indexes:
        pos = grid.index_to_pos(index)
        grid[pos] = "#"
    print(f"{grid}")
