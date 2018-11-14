from images2gif import writeGif
from distances import Grid, grid_to_img
from sidewinder import sidewinder_maze_iterator
from binary_tree import binary_tree_maze_iterator

if __name__ == '__main__':
  grid = Grid(12, 12)

  images = []
  
  for grid in sidewinder_maze_iterator(grid):
    images.append(grid_to_img(grid))

  writeGif('sidewinder_maze_build.gif', images, 0.01)
