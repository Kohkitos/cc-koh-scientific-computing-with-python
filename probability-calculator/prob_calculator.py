import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **vars):
      self.contents = []
      for key, value in vars.items():
          for i in range(value):
              self.contents.append(key)
        
  def draw(self, balls):
      if (balls > len(self.contents)):
          return self.contents
      ans = []
      for i in range(balls):
        ans.append(self.contents.pop(random.randrange(0, (len(self.contents)))))
      return ans

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for i in range(num_experiments):
      temp_hat = copy.deepcopy(hat)
      temp_drawn = temp_hat.draw(num_balls_drawn)
      temp_exp = copy.deepcopy(expected_balls)
    
      for item in temp_drawn:
          if (item in temp_exp):
              temp_exp[item] -= 1
            
      if(all(value <= 0 for value in temp_exp.values())):
          success += 1
        
  return (success / num_experiments)