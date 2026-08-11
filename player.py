import pygame as pg

pg.init()

class Player: 
  def __init__(self) -> None:
    self.SIZE: int = 64
    self.SPEED: int = 2

    self.position: pg.math.Vector2 = pg.math.Vector2(0, 0)
    self.direction: pg.math.Vector2 = pg.math.Vector2(0, 0)

    self.rect: pg.Rect = pg.Rect(
      self.position.x, 
      self.position.y, 
      self.SIZE, 
      self.SIZE
    )

  def move(self, keys): 
    self.direction.x = 0

    if keys[pg.K_a]: 
      self.direction.x = -1
    if keys[pg.K_d]: 
      self.direction.x = 1

    self.position.x += self.SPEED * self.direction.x
    self.rect.x = self.position.x

  def update(self): 
    keys = pg.key.get_pressed()

    self.move(keys)

  def draw(self, master: pg.Surface) -> None: 
    pg.draw.rect(master, (189, 189, 189), self.rect)
