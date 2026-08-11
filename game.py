import pygame as pg

from player import Player

pg.init()

class Game: 
  def __init__(self) -> None:
    self.running: bool = False

    self.window: pg.Surface = pg.display.set_mode((800, 800))

    self.player: Player = Player()

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
      self.player.draw(self.window)

      pg.display.flip()

