import pygame as pg

import csv

from tile import Tile

pg.init()

class TileMap: 
  def __init__(self, path: str): 
    self.path: str = path

    self.start_x = 0
    self.start_y = 0

    self.tiles: list[Tile] = []
    self.level: list[str] = []

    with open(self.path) as filename: 
      content = csv.reader(filename, delimiter = " ")

      for row in content: 
        self.level.append(row)

  def gen_tilemap(self) -> list[Tile]: 
    y: int = 0

    for row in self.level: 
      x: int = 0

      for char in row: 
        if char == "1": 
          # 1 = ground 
          self.tiles.append(Tile(x * 32, y * 32))

        x += 1
      y += 1

    return self.tiles

  def draw(self, master: pg.Surface): 
    for tile in self.tiles: 
      pg.draw.rect(master, tile.get_color(), tile.get_rect())
