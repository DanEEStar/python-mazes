from random import choice
from grid import Grid, grid_to_img

def binary_tree_maze(grid):
  for cell in grid.each_cell():
    neighbors = []
    if cell.north:
      neighbors.append(cell.north)
    if cell.east:
      neighbors.append(cell.east)
    
    if len(neighbors) > 0:
      neighbor = choice(neighbors)
      cell.link(neighbor)
  return grid


if __name__ == '__main__':
  g = Grid(12, 12)
  img = grid_to_img(g)
  img.show()
  g = binary_tree_maze(g)
  print(g)
  img = grid_to_img(g)
  img.show()
  
  
