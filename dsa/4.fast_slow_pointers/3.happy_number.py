class HappyNumber:
  
  def is_happy_number(self, num):
    slow, fast = num, num
    while True:
      slow = self.get_next_number(slow)
      fast = self.get_next_number(self.get_next_number(fast))
      if fast == 1:
        return True
      elif slow == fast:
        return False
  
  def get_next_number(self, x):
    ret = 0
    while x > 0:
      digit = x % 10
      x //= 10
      ret += digit ** 2
    return ret
      
