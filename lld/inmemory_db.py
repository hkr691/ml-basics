from typing import List
import copy

class InMemoryDB:
  def __init__(self):
    self.db = {}
    self.backups = {}
  
  def _expire_if_needed(self, ts: int, key: str, field: str):
    if key in self.db and field in self.db[key]:
      val, expire_at = self.db[key][field]
      if ts >= expire_at:
        del self.db[key][field]
        if not self.db[key]:
          del self.db[key]
        return True
    return False
   
  def _sweep_all_expired(self, ts: int):
    keys = list(self.db.keys())
    for key in keys:
      fields = list(self.db[key].keys())
      for field in fields:
        self._expire_if_needed(ts, key, field)         
  
  def set(self, ts: int, key: str, field: str, value: int):
    if key not in self.db:
      self.db[key] = {}
    
    self.db[key][field] = (value, float('inf'))
  
  def set_with_ttl(self, ts: int, key: str, field: str, value: int, ttl: int):
    if key not in self.db:
      self.db[key] = {}
    
    self.db[key][field] = (value, ts + ttl)
  
  def compare_and_set(self, ts: int, key: str, field: str, expected_value: int, new_value: int):
    self._expire_if_needed(ts, key, field)
    if key not in self.db or field not in self.db[key]:
      return False
    
    current_value, expire_at = self.db[key][field]
    if current_value == expected_value:
      self.db[key][field] = (new_value, expire_at)
      return True
    return False
  
  def compare_and_delete(self, ts: int, key: str, field: str, expected_value: int):
    self._expire_if_needed(ts, key, field)
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
    fields = list(self.db[key].keys())
    for field in fields:
      self._expire_if_needed(ts, key, field)
    if key not in self.db:
      return []
    sorted_fields = sorted(self.db[key].keys())
    return [f"{field}({self.db[key][field][0]})" for field in sorted_fields]
  
  def scan_by_prefix(self, ts: int, key: str, prefix: str):
    if key not in self.db:
      return []
    fields = list(self.db[key].keys())
    for field in fields:
      self._expire_if_needed(ts, key, field)
    if key not in self.db:
      return []
    valid_fields = [field for field in self.db[key].keys() if field.startswith(prefix)]
    sorted_fields = sorted(valid_fields)
    return [f"{field}({self.db[key][field][0]})" for field in sorted_fields]

  def backup(self, ts: int):
    self._sweep_all_expired(ts)
    self.backups[ts] = copy.deepcopy(self.db)
    return len(self.backups[ts])
  
  def restore(self, ts: int, ts_to_restore: int):
    if ts_to_restore not in self.backups:
      return False
    self.db = copy.deepcopy(self.backups[ts_to_restore])
    self._sweep_all_expired(ts)
    return True
