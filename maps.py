import os
from tiles import Tile
#from tiles import tile_definitions

def load_map(filepath: str) -> list: 
    """
    Returns the map as a list of lists of single characters
    """
    
    map = []
    
    with open(filepath) as file:
        raw = file.read()
    
    for line in raw.split('\n'):
        row = []
        for char in line:
            row.append(char)
        map.append(row)
    
    return map

def construct_tilemap(map: list) -> list:
    tilemap = []
    for row in map:
        tile_row = []
        for char in row:
            tile_row.append(Tile(char))
        tilemap.append(tile_row)
    
    return tilemap