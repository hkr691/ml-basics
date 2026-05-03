class ZingzagConversion:
  def output_zigzag_string(self, s: str, numRows: int) -> str:
    if numRows == 1:
      return s
    
    res = []
    for row in range(numRows):
      incr = (numRows - 1) * 2
      for i in range(row, len(s), incr):
        res.append(s[i])
        if row > 0 and row < numRows - 1 and i + incr - 2 * row < len(s):
          res.append(s[i + incr - 2 * row])
    return ''.join(res)


s = 'paypalishiring'
n = 4
zizzag = ZingzagConversion()
print(zizzag.output_zigzag_string(s, n))
