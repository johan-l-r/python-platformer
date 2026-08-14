import pygame as pg

from player import Player
from tilemap import TileMap
from tile import Tile

pg.init()

class Game: 
  def __init__(self) -> None:
    self.running: bool = False

    self.window: pg.Surface = pg.display.set_mode((832, 832))

    self.player: Player = Player()
    self.tilemap: TileMap = TileMap("./levels/lvl.csv")

    self.map: list[Tile] = self.tilemap.gen_tilemap()

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
      self.player.update()

      # draw 
      self.player.draw(self.window)
      self.tilemap.draw(self.window)

      pg.display.flip()

