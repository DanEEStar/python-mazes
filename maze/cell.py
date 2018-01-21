class Cell:
  def __init__(self, row, column):
    self.row = row
    self.column = column
    self._links = set()
    
  def link(self, cell, bidi=True):
    self._links.add(cell)
    if bidi:
      cell.link(self, False)
    return self
    
  def unlink(self, cell, bidi=True):
    self._links.discard(cell)
    if bidi:
      cell.unlink(self, False)
    return self
    
  def linked(self, cell):
    return cell in self._links
    
  def links(self):
    return self._links
    
  def __str__(self):
    return '({}, {})'.format(self.row, self.column)


import unittest

class CellTestCase(unittest.TestCase):
  def test_link_unlink(self):
    c1 = Cell(1, 1)
    c2 = Cell(2, 2)
    
    self.assertFalse(c1.linked(c2))
    
    c1.link(c2)
    self.assertTrue(c1.linked(c2))
    
    c2.unlink(c1)
    self.assertFalse(c1.linked(c2))
    

if __name__ == '__main__':
  unittest.main()
