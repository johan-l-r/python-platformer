import pygame as pg

pg.init()

class Player: 
  def __init__(self) -> None:
    self.SIZE: int = 64
    self.position: pg.math.Vector2 = pg.math.Vector2(0, 0)

    self.rect: pg.Rect = pg.Rect(
      self.position.x, 
      self.position.y, 
      self.SIZE, 
      self.SIZE
    )

  def draw(self, master: pg.Surface) -> None: 
    pg.draw.rect(master, (189, 189, 189), self.rect)
