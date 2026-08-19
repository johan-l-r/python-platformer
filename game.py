import pygame as pg

from player import Player
from tilemap import TileMap

pg.init()

class Game: 
  def __init__(self) -> None:
    self.running: bool = False

    self.window: pg.Surface = pg.display.set_mode((832, 832))

    self.player: Player = Player()
    self.tilemap: TileMap = TileMap("./levels/lvl.csv")

  def check_collisions(self): 
    for tile in self.tilemap.get_tiles(): 
      # Y collisions
      if tile.get_rect().collidepoint(self.player.get_rect().bottomleft): 
        self.player.velocity.y = 0
        self.player.get_position().y = tile.get_rect().top
        self.player.get_rect().bottom = self.player.get_position().y

      # left collisions
      if tile.get_rect().collidepoint(self.player.get_rect().topleft): 
        self.player.get_position().x = tile.get_rect().right
        self.player.get_rect().x = self.player.get_position().x

      # right collisions
      if tile.get_rect().collidepoint(self.player.get_rect().topright): 
        self.player.get_position().x = tile.get_rect().left - 32
        self.player.get_rect().x = self.player.get_position().x
      
  def update(self): 
    self.player.update()
    self.check_collisions()

  def draw(self): 
    self.player.draw(self.window)
    self.tilemap.draw(self.window)

  def run(self) -> None: 
    self.running = True

    while self.running: 
      for event in pg.event.get(): 
        if event.type == pg.QUIT: 
          self.running = False

      self.window.fill((8, 8, 8))

      # update 
      self.update()

      # draw 
      self.draw()

      pg.display.flip()

