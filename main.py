import random

from grid import Grid
from vec2 import Vec2

#
def random_positions(grid: Grid, n: int):
    square_positions = []
    square_indexes = list(range(grid.width * grid.height))
    assert n <= len(square_indexes)
    for i in range(n):
        idx = random.choice(range(len(square_indexes)))
        square_index = square_indexes[idx]
        print(square_indexes)
        print(square_index)
        del square_indexes[idx] # < Là on supprime directement le square_index déterminé par idx
        print(square_indexes)
        square_positions.append(grid.index_to_pos(square_index))
    #...
    square_indexes = list(range(grid.width * grid.height))
    square_index = random.choice(square_indexes)
    print(square_indexes)
    print(square_index)
    square_indexes.remove(square_index) # < On doit parcourir toute la liste pour supprimer le square_index
    print(square_indexes)
    return square_positions

if __name__ == "__main__":
    grid = Grid(Vec2(3, 2), ".")
    positions = random_positions(grid, 2)
    print(f"{positions}")
    #-----
    grid = Grid(Vec2(12, 6), ".")
    rng_seed = random.randint(0, 100)
    print(f"seed: {rng_seed}")
    random.seed(rng_seed)
    indexes = list(range(grid.width * grid.height))
    nb_root_obstacles = 10
    chosen_indexes = sorted(random.choices(indexes, k=nb_root_obstacles))
    print(chosen_indexes)
    for index in chosen_indexes:
        pos = grid.index_to_pos(index)
        grid[pos] = "#"
    print(f"{grid}")
