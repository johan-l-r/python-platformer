import pygame as pg

pg.init()

class Tile: 
  def __init__(self, x: int, y: int): 
    self.SIZE: int = 32

    self.color: tuple[int] = (189, 189, 189)

    self.rect: pg.Rect = pg.Rect(x, y, self.SIZE, self.SIZE)

  def draw(self, master: pg.Surface): 
    pg.draw.rect(master, (189, 189, 189), self.rect)

  def get_rect(self) -> pg.Rect: return self.rect
  def get_color(self) -> tuple[int]: return self.color
