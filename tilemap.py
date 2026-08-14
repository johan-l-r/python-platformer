import pygame as pg

import csv

pg.init()

class TileMap: 
  def __init__(self, path: str): 
    self.path: str = path

  def read(self): 
    with open(self.path) as file: 
      level = csv.reader(file, delimiter = " ")

