class Fruit:
  def __init__(self, apple = 5, banana = 10):
    self.apple = apple
    self.banana = banana
eat = Fruit()
 
# returns __dict__ of the eat object
 
print(vars(eat))