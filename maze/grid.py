from cell import Cell
from PIL import Image, ImageDraw


class Grid:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.grid = self.prepare_grid()
    self.configure_cells()
    
  def prepare_grid(self):
    result = []
    for row in range(self.rows):
      row_cells = []
      for column in range(self.columns):
        row_cells.append(Cell(row, column))
      result.append(row_cells)
    return result
    
  def configure_cells(self):
    for cell in self.each_cell():
      row = cell.row
      col = cell.column
      cell.north = self[row - 1, col]
      cell.south = self[row + 1, col]
      cell.east = self[row, col + 1]
      cell.west = self[row, col - 1]
      
  def each_row(self):
    for row in self.grid:
      yield row
      
  def each_cell(self):
    for row in self.each_row():
      for cell in row:
        yield cell
        
  def __len__(self):
    return self.rows * self.columns
    
  def __iter__(self):
    return self.each_cell()
        
  def __getitem__(self, t):
    row, column = t
    if row < 0 or row >= self.rows:
      return None
    if column < 0 or column >= len(self.grid[row]):
      return None
    return self.grid[row][column]
    
  def __str__(self):
    return grid_ascii_renderer(self, lambda c: '   ')


def grid_ascii_renderer(grid, cell_body):
  output = "+" + "---+" * grid.columns + "\n"
    
  for row in grid.each_row():
    top = "|"
    bottom = "+"
    for cell in row:
      body = cell_body(cell)
      east_boundary = " " if cell.linked(cell.east) else "|"
      top += body + east_boundary
        
      south_boundary = "   " if cell.linked(cell.south) else "---"
      bottom += south_boundary + "+"
        
    output += top + "\n"
    output += bottom + "\n"
  return output


def grid_to_img(grid, cell_background_color=None, resize_factor=4, cell_size=10, highlight_current=None):
   if cell_background_color == None:
     cell_background_color = lambda x: (255, 255, 255)
   
   img_width = cell_size * grid.columns 
   img_height = cell_size * grid.rows
   
   background = 255
   wall = 0
   
   img = Image.new("RGB", (img_width+1, img_height+1), "white")
   draw = ImageDraw.Draw(img)
   
   for mode in ('background', 'border'):
     for cell in grid:
       x1 = cell.column * cell_size 
       y1 = cell.row * cell_size 
       x2 = (cell.column + 1) * cell_size 
       y2 = (cell.row + 1) * cell_size
     
       if mode == 'background':
         color = cell_background_color(cell)
         if color:
           draw.rectangle((x1, y1, x2, y2), fill=color)
         if highlight_current == cell:
           draw.rectangle((x1+2, y1+2, x2-2, y2-2), outline=(255,0,0))
           
       if mode == 'border':
         if not cell.north:
           draw.line((x1, y1, x2, y1), fill=wall)
       
         if not cell.west:
           draw.line((x1, y1, x1, y2), fill=wall)
       
         if not cell.linked(cell.south):
           draw.line((x1, y2, x2, y2), fill=wall)
       
         if not cell.linked(cell.east):
           draw.line((x2, y1, x2, y2), fill=wall)
   
   del draw
   
   img = img.resize((img_width*resize_factor+resize_factor, 
     img_height*resize_factor+resize_factor))
   return img


    
import unittest

class GridTestCase(unittest.TestCase):
  def test_init(self):
    grid = Grid(5,5)
    print(grid)
    img = grid_to_img(grid, resize_factor=2)
    img.show()


if __name__ == '__main__':
  unittest.main()
  
