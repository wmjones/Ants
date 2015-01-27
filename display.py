import math
from PIL import Image, ImageDraw

class HexagonGenerator(object):
  """Returns a hexagon generator for hexagons of the specified size."""
  def __init__(self, edge_length):
    self.edge_length = edge_length
    
  def __call__(self, row, col):
    center_x = math.sqrt(3) * self.edge_length * (col + row * .5)
    center_y = 3 * self.edge_length * row * .5
    
    #offset so that it isnt cut off
    for angle in [30, 90, 150, 210, 270, 330]:
      x = center_x + math.cos(math.radians(angle)) * self.edge_length
      y = center_y + math.sin(math.radians(angle)) * self.edge_length
      yield x
      yield y

def main():
    #format image size based on hex size and number
  image = Image.new('RGB', (800, 800), 'white')
  draw = ImageDraw.Draw(image)
  hexagon_generator = HexagonGenerator(20)
  for row in range(20):
      for col in range(20):
          hexagon = hexagon_generator(row, col)
          draw.polygon(list(hexagon), outline='black', fill='red')
  
  image.show()

main()

#perhaps set up so that I call it from main.py
