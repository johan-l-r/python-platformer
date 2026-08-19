import pygame as pg

import csv

from tile import Tile

pg.init()

class TileMap: 
  def __init__(self, path: str): 
    self.path: str = path

    self.start_x = 0
    self.start_y = 0

    self.tiles: list[Tile] = self.gen_tilemap()

  def read_level(self): 
    lines: list[str] = []

    with open(self.path) as filename: 
      content = csv.reader(filename, delimiter = " ")

      for row in content: 
        lines.append(row)

    return lines

  def gen_tilemap(self) -> list[Tile]: 
    tiles = []
    map: list[str] = self.read_level()

    y: int = 0

    for row in map: 
      x: int = 0

      for char in row: 
        if char == "1": 
          # 1 = ground 
          tiles.append(Tile(x * 32, y * 32))

        x += 1
      y += 1

    return tiles

  def draw(self, master: pg.Surface): 
    for tile in self.tiles: 
      pg.draw.rect(master, tile.get_color(), tile.get_rect())

  def get_tiles(self) -> list[Tile]: return self.tiles
