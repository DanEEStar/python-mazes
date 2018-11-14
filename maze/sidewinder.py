from random import choice, randint
from grid import Grid, grid_to_img

def sidewinder_maze_iterator(grid):
  run = []
  for cell in grid.each_cell():
    run.append(cell)
    
    at_eastern_boundary = (cell.east == None)
    at_northern_boundary = (cell.north == None)
    
    should_close_out = (at_eastern_boundary or 
      (not at_northern_boundary and randint(0, 1) == 0))
    
    if should_close_out:
      member = choice(run)
      if member.north:
        member.link(member.north)
      run = []
    else:
      cell.link(cell.east)
    yield grid
    
  return grid
  
def sidewinder_maze(grid):
  for grid in sidewinder_maze_iterator(grid):
    pass
  return grid


if __name__ == '__main__':
  g = Grid(12, 12)
  g = sidewinder_maze(g)
  img = grid_to_img(g)
  img.show()
