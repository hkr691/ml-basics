from typing import List

class InMemoryDB:
  def __init__(self):
    self.db = {}
  
  def _expire_if_needed(self, ts: int, key: str, field: str):'
    if key in self.db and field in self.db[key]:
      val, expire_at = self.db[key][field]
      if ts >= expire_at:
        del self.db[key][field]
        if not self.db[key]:
          del self.db[key]
        return True
    return False
  
  def set(self, ts: int, key: str, field: str, value: int):
    if key not in self.db:
      self.db[key] = {}
    
    self.db[key][field] = (value, float('inf'))
  
  def set_with_ttl(self, key: str, field: str, ttl: int):
    if key not in self/db:
      self.db[key] = {}
    
    self.db[key][field] = (value, ts + ttl)
  
  def compare_and_set(self, ts: int, key: str, field: str, expected_value: int, new_value: int):
    self._expire_if_needed(ts, key, field)
    if key not in self.db or field not in self.db[key]:
      return False
    
    current_value = self.db[key][field][0]
    if current_value == expected_value:
      self.db[key][field] = (new_value, float('inf'))
      return True
    return False
  
  def compare_and_delete(self, ts: int, key: str, field: str, expected_value: int):
    self._exipre_if_needed(ts, key, field)
    if key not in self.db or field not in self.db[key]:
      return False
    current_value = self.db[key][field][0]
    if current_value == expected_value:
      del self.db[key][field]
    
      if not self.db[key]:
        del self.db[key]
      return True
    return False
    
  def get(self, ts: int, key: str, field: str):
    self._expire_if_needed(ts, key, field)
    if key not in self.db or field not in self.db[key]:
      return None
    return self.db[key][field][0]
  
  def scan(self, ts: int, key: str):
    if key not in self.db:
      return []
    sorted_fields = sorted(self.db[key].keys())
    return [f"{field}({self.db[key][field]})" for field in sorted_fields]
  
  def scan_by_prefix(self, ts: int, key: str, prefix: str):
    if key not in self.db:
      return []
    valid_fields = [field for field in self.db[key].keys() if field.startswith(prefix)]
    sorted_fields = sorted(valid_fields)
    return [f"{field}({self.db[key][field]})" for field in sorted_fields]
