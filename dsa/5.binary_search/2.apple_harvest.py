"""
Bobby has an orchard of apple trees, and each tree has a certain number of apples on it.

Bobby wants to collect all the apples by the end of the day by collecting a fixed number of apples per hour. He can only harvest apples from one tree per hour - if he finishes collecting apples from a tree before the hour is up, he must wait until the next hour to move to the next tree.

    For example, if there are 3 apples on a tree and Bobby collects 1 apple per hour, it will take him 3 hours to finish collecting the apples on that tree.
    If he harvests 2 apples per hour, it will take him 2 hours to finish collecting all the apples on that tree (he waits until the hour is up even though he finishes early).

Write a function to determine the slowest rate of apples Bobby can harvest per hour to finish the job in at most 'h' hours. The input to the function is an array of integers representing the number of apples on each tree and an integer 'h' representing the number of hours Bobby has to finish the job within.

Example 1:

Input:

apples = [3, 6, 7], h = 8

Output: 3

Explanation:

    1 apple per hour: 3 hours for first tree, 6 hours the second tree, and 7 hours for third tree. This totals 16 hours, which is more than the 8 hours he has to finish the job. NOT VALID.
    2 apples per hour: 2 + 3 + 4 = 9 hours, which is more than the 8 hours he has to finish the job. NOT VALID.
    3 apples per hour: 1 + 2 + 3 = 6 hours, which is less than the 8 hours he has to finish the job. VALID.
    4 apples per hour: 1 + 2 + 2 = 5 hours, which is less than the 8 hours he has to finish the job. VALID.
    5 apples per hour: 1 + 2 + 2 = 5 hours, which is less than the 8 hours he has to finish the job. VALID.

"""

def get_min_harvest_rate(apple_trees, h):
  if not apple_trees:
    return 0
  
  def timeTaken(rate):
    time = 0
    for apples in apple_trees:
      # rate -1 included in numerator for ceil division - same achieved using math.ceil
      time += (apples + rate - 1) // rate
    return time
  
  l, r = 1, max(apple_trees)
  
  while l < r:
    mid = (l + r) // 2
    if timeTaken(mid) > h:
      l = mid + 1
    else:
      r = mid
  return l
