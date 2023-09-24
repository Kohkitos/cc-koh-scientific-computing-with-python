class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width
    
  def __repr__(self):
    return ('Rectangle(width=' + str(self.width) + ', height=' + str(self.height) +')')
  
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if (self.width >= 50) | (self.height >= 50):
        return 'Too big for picture.'
    ans = ''
    for i in range(self.height):
        for j in range(self.width):
            ans += '*'
        ans += '\n'
    return ans

  def get_amount_inside(self, temp):
      ans = self.get_area() / temp.get_area()
      return int(ans)

class Square(Rectangle):
  def __init__(self, side):
    self.height = side
    self.width = side
    
  def __repr__(self):
    return ('Square(side=' + str(self.height) + ')')

  def set_side(self, side):
    self.width = side
    self.height = side
  
  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.height = side
    self.width = side