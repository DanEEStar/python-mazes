from grid import Grid, grid_ascii_renderer, grid_to_img
from binary_tree import binary_tree_maze
from sidewinder import sidewinder_maze


def dijkstra_iterator(cell):
  visited = {cell}
  frontier = {cell}
  while len(frontier) > 0:
    new_frontier = set()
    for cell in frontier:
      for link in cell.links():
        if link in visited:
          continue
        visited.add(cell)
        new_frontier.add(link)
        yield (cell, link)
    frontier = new_frontier
    
    
def depth_first_iterator(cell, visited=None):
  if visited is None:
    visited = {cell}

  for link in cell.links():
    if link in visited:
      continue
    
    visited.add(link)
    yield cell, link
    yield from depth_first_iterator(link, visited)


def cell_distances(cell):
  distances = {cell: 0}
  
  for cell, link in dijkstra_iterator(cell):
    distances[link] = distances[cell] + 1
  
  return distances
  
  
def shortest_path(start_cell, goal_cell):
  current = goal_cell
  
  distances = cell_distances(start_cell)
  breadcrumbs = {current: distances[current]}
  
  while current != start_cell:
    for neighbor in current.links():
      if distances[neighbor] < distances[current]:
        breadcrumbs[neighbor] = distances[neighbor]
        current = neighbor
  return breadcrumbs
  

def longest_path(grid):
  distances = cell_distances(grid[0,0])
  start = max(distances, key=distances.get)
  new_distances = cell_distances(start)
  goal = max(new_distances, key=new_distances.get)
  
  return shortest_path(start, goal)
  

def base_n(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
    
  
def grid_distances_renderer(grid, distances):
  def cell_body(cell):
    if cell in distances:
      symbol = base_n(distances[cell], b=36)
      if distances[cell] >= 36:
        symbol = '*'
      return ' {} '.format(symbol)
    return '   '
  
  return grid_ascii_renderer(grid, cell_body)
  
def grid_to_img_color_distances(grid, distances, max_value=None, highlight_current=None):
  if max_value is None:
    max_value = max(distances.values())
  
  def cell_color(cell):
    if cell in distances:
      intensity = (max_value - distances[cell]) / max_value
      dark = int(255 * intensity)
      bright = 128 + int(127 * intensity)
      return (dark, dark, bright)
  return grid_to_img(grid, cell_color, highlight_current=highlight_current)
  
    
import unittest

class GridTestCase(unittest.TestCase):
  def test_init(self):
    grid = Grid(12,12)
    grid = sidewinder_maze(grid)
    print(grid)
    
    #print(grid_distances_renderer(grid, cell_distances(grid[0,0])))
    
    #print(grid_distances_renderer(grid, shortest_path(grid[0,0], grid[grid.rows-1, 0])))
    
    print(grid_distances_renderer(grid, longest_path(grid)))
    
    img = grid_to_img_color_distances(grid, cell_distances(grid[grid.rows//2, grid.columns//2]))
    img.show()
    
    for c in depth_first_iterator(grid[0,0]):
      #print(c)
      pass

if __name__ == '__main__':
  unittest.main()
