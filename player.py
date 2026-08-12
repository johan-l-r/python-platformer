import pygame as pg

pg.init()

class Player: 
  def __init__(self) -> None:
    self.SIZE: int = 64
    self.SPEED: int = 2

    self.GRAVITY: float = 0.2
    self.vectical_speed: float = 0
    self.JUMP_FORCE: int = 12

    self.is_on_ground: bool = False

    self.position: pg.math.Vector2 = pg.math.Vector2(0, 0)
    self.direction: pg.math.Vector2 = pg.math.Vector2(0, 1)

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

  def jump(self, keys): 
    if keys[pg.K_SPACE] and self.is_on_ground: 
      self.is_on_ground = False
      self.direction.y = -1

      self.vectical_speed = self.JUMP_FORCE

    if not self.is_on_ground: 
      if self.direction.y == -1: 
        self.vectical_speed -= self.GRAVITY

        if self.vectical_speed <= 0: 
          self.direction.y = 1
          self.vectical_speed = 0
      
      if self.direction.y == 1: 
        self.vectical_speed += self.GRAVITY

    else: 
      self.direction.y = 0
      self.vectical_speed = 0

    self.position.y += self.vectical_speed * self.direction.y
    self.rect.y = self.position.y

  def collide(self): 
    if self.position.y >= 505: # provisional logic 
      self.is_on_ground = True

      self.direction.y = 0

      self.position.y = 505
      self.rect.y = self.position.y

  def update(self): 
    keys = pg.key.get_pressed()

    self.move(keys)
    self.jump(keys)
    self.collide()

  def draw(self, master: pg.Surface) -> None: 
    pg.draw.rect(master, (189, 189, 189), self.rect)
