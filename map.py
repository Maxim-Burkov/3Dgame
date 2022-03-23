from settings import *

text_map = [
    "111111111111",
    "100000001111",
    "101110100111",
    "101000110011",
    "111100100001",
    "100000001111",
    "100111000011",
    "111111111111"
]

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == '1':
            world_map.add((i * TILE, j * TILE))