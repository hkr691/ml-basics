class File:
  def __init__(self, name: str, size: int, user_id: str = "admin"):
    self.name = name
    self.size = size
    self.user_id = user_id

class User:
  def __init__(self, user_id: str, capacity: int):
    self.user_id = user_id
    self.capacity = capacity
    self.files = set()
    self.backup = None

class CloudStorage:
  def __init__(self):
    self.storage = {}
    self.users = {}
  
  def add_file(self, name: str, size: int):
    if name in self.storage:
      return "false"
    f = File(name, size)
    self.storage[name] = f
    return "true"
  
  def get_size(self, name: str) -> str:
    if name not in self.storage:
      return ""
    return str(self.storage[name].size)
    
  def delete_file(self, name: str) -> str:
    if name not in self.storage:
      return ""
    f = self.storage.pop(name)
    if f.user_id in self.users:
      user = self.users[f.user_id]
      user.capacity += f.size
      user.files.remove(f)
    return (str(f.size))
  
  def n_largest(self, prefix: str, n: str) -> str:
    res, n = [], int(n)
    for f in self.storage.values():
      if f.name.startswith(prefix):
        res.append(f)
    if len(res) == 0:
      return ""
    res.sort(key=lambda x: (-x.size, x.name))
    return ", ".join([f.name for f in res[: n]])
  
  def add_user(self, user_id: str, capacity: str) -> str:
    if user_id in self.users:
      return "false"
    self.users[user_id] = User(user_id, int(capacity))
    return "true"
  
  def add_file_by(self, user_id: str, name: str, size: int) -> str:
    if name in self.storage or user_id not in self.users:
      return ""
    user = self.users[user_id]
    f = File(name, size, user_id)
    if f.size > user.capacity:
      return ""
    self.storage[name] = f
    user.capacity -= size
    user.files.add(f)
    return str(user.capacity)
  
  def merge_user(self, user_id1, user_id2):
    if user_id1 not in self.users or user_id2 not in self.users or user_id1 == user_id2:
      return ""
    user1, user2 = self.users[user_id1], self.users[user_id2]
    for f in user2.files:
      f.user_id = user1.user_id
    user1.files.update(user2.files)
    user1.capacity += user2.capacity
    del self.users[user_id2]
    return str(user1.capacity)
  
  def backup(self, user_id):
    if user_id not in self.users:
      return ""
    user = self.users[user_id]
    user.backup = user.files.copy()
    return str(len(user.files))
  
  def restore(self, user_id):
    if user_id not in self.users:
      return ""
    user = self.users[user_id]
    if user.backup is None:
      return "0"
    for f in user.files.copy():
      self.delete_file(f.name)
    ct = 0
    for f in user.backup:
      if f.name not in self.storage:
        res = self.add_file_by(user_id, f.name, f.size)
        if res != "":
          ct += 1
    return str(ct)
