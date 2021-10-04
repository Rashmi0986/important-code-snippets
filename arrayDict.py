Create an array dictionary (without using built-in dict lib)
# https://blog.devgenius.io/data-structures-and-algorithms-are-they-really-necessary-d8f29df2125
class ArrayDict:
  def __init__(self):
    self.indices = []
    self.values = []

  def get(self, key):
    if key not in self.indices:
      return None
    else:
      index = self.indices.index(key)
      return self.values[index]
  
  def set(self, key, value):
    if key not in self.indices:
      self.indices.append(key)
      self.values.append(value)
    else:
      index = self.indices.index(key)
      self.values[index] = value
      
      
      
      
      
