import pygame as pg

pg.init()

class Player: 
  def __init__(self) -> None:
    self.SIZE: int = 64
    self.SPEED: int = 1

    self.GRAVITY: float = 0.2
    self.vectical_speed: float = 0
    self.JUMP_FORCE: int = 10

    self.is_on_ground: bool = False

    self.position: pg.math.Vector2 = pg.math.Vector2(0, 0)
    self.direction: pg.math.Vector2 = pg.math.Vector2(0, 0)
    self.acceleration: pg.math.Vector2 = pg.math.Vector2(0, 0) 
    self.velocity: pg.math.Vector2 = pg.math.Vector2(0, 0)

    self.rect: pg.Rect = pg.Rect(
      self.position.x, 
      self.position.y, 
      self.SIZE, 
      self.SIZE
    )

  def move(self, keys): 
    # apply gravity constantly 
    self.acceleration = pg.math.Vector2(0, self.GRAVITY)
    self.direction.x = 0

    if keys[pg.K_a]: 
      self.direction.x = -1
    elif keys[pg.K_d]: 
      self.direction.x = 1
    else: 
      self.direction.x = 0

    self.acceleration.x = self.SPEED * self.direction.x
    self.acceleration.x -= self.velocity.x

    self.velocity += self.acceleration
    self.position += self.velocity

    self.rect.bottomleft = self.position

  def jump(self, keys): 
    if keys[pg.K_SPACE] and self.is_on_ground:
      self.velocity.y = -self.JUMP_FORCE
      self.is_on_ground = False

  def collide(self): 
    if self.position.y >= 500: # provisional logic 
      self.is_on_ground = True

      self.position.y = 500
      self.rect.bottomleft = self.position

  def update(self): 
    keys = pg.key.get_pressed()

    self.move(keys)
    self.jump(keys)
    self.collide()

  def draw(self, master: pg.Surface) -> None: 
    pg.draw.rect(master, (189, 189, 189), self.rect)
