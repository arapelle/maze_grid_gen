import filecmp
import os
import shutil
from pathlib import Path
from unittest import TestCase

from neighborhood import square_neighbor_positions, ortho_neighbor_positions
from vec2 import Vec2


class TestNeighborhood(TestCase):
    def test__square_neighbor_positions__0_0_d1__expected_list(self):
        distance = 1
        positions = square_neighbor_positions(Vec2(0, 0), distance)
        expected_positions = []
        self.assertEqual(positions, expected_positions)

    def test__ortho_neighbor_positions__0_0_d1__expected_list(self):
        distance = 1
        positions = ortho_neighbor_positions(Vec2(0, 0), distance)
        expected_positions = []
        self.assertEqual(positions, expected_positions)

    def test__square_neighbor_positions__0_0_d2__expected_list(self):
        distance = 2
        positions = square_neighbor_positions(Vec2(0, 0), distance)
        expected_positions = []
        self.assertEqual(positions, expected_positions)

    def test__ortho_neighbor_positions__0_0_d2__expected_list(self):
        distance = 2
        positions = ortho_neighbor_positions(Vec2(0, 0), distance)
        expected_positions = []
        self.assertEqual(positions, expected_positions)
