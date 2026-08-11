import pygame as pg

pg.init()

class Game: 
  def __init__(self) -> None:
    self.running: bool = False

    self.window: pg.Surface = pg.display.set_mode((800, 800))

  def update(self): pass
  def draw(self): pass

  def run(self) -> None: 
    self.running = True

    while self.running: 
      for event in pg.event.get(): 
        if event.type == pg.QUIT: 
          self.running = False

      self.window.fill((8, 8, 8))

      # update 

      # draw 

      pg.display.flip()

