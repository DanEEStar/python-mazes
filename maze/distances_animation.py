from images2gif import writeGif
from distances import Grid, grid_to_img_color_distances, cell_distances, longest_path, dijkstra_iterator, depth_first_iterator
from sidewinder import sidewinder_maze
from binary_tree import binary_tree_maze

if __name__ == '__main__':
  grid = Grid(12, 12)
  grid = sidewinder_maze(grid)
  max_grid_value = max(longest_path(grid).values())

  images = [
    grid_to_img_color_distances(
      grid, cell_distances(link), max_grid_value, highlight_current=link)
    for c, link in depth_first_iterator(grid[0, 0])
  ]

  writeGif('depthfirst.gif', images, 0.01)

