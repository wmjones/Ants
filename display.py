import math
from PIL import Image, ImageDraw

class HexagonGenerator(object):
  """Returns a hexagon generator for hexagons of the specified size."""
  def __init__(self, edge_length):
    self.edge_length = edge_length
    
  def __call__(self, row, col):
    center_x = math.sqrt(3) * self.edge_length * (col + row * .5)
    center_y = 3 * self.edge_length * row * .5
    
    #i should offset so that it isnt cut off
    for angle in [30, 90, 150, 210, 270, 330]:
      x = center_x + math.cos(math.radians(angle)) * self.edge_length
      y = center_y + math.sin(math.radians(angle)) * self.edge_length
      yield x
      yield y

def graphHexGrid(x_length, y_length, edge_length, matrix,t):
    #format image size based on hex size and number
  image = Image.new('RGBA', (x_length, y_length), 'white')
  draw = ImageDraw.Draw(image)
  hexagon_generator = HexagonGenerator(edge_length)
  for row in range(len(matrix)):
      for col in range(len(matrix)):
          hexagon = hexagon_generator(row, col)
          if matrix[row][col]==1:
              draw.polygon(list(hexagon), fill='black')
          else:
              draw.polygon(list(hexagon), outline='black', fill='white')
  image.save('Frame' + str(t) + '.GIF', 'GIF',transparency=0)

n=2*4
myWorld=[]
myWorld=[[0 for j in range(n)] for i in range(n)]

#graphHexGrid(500,500,10,myWorld)
#perhaps set up so that I call it from main.py
#[i-1,j],[i-1,j+1],[i,j+1],[i+1,j],[i+1,j-1],[i,j-1]
