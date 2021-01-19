with open('w4rmup.txt', 'r') as f:
    c = f.read()

c = c.replace('@', '0').replace('$', '1')       # @ -> 0, $ -> 1
c = int(c, 2)                                   # str to int
c = c.to_bytes(c.bit_length() // 8 + 1, 'big')  # int to bytes
c = c.decode('ascii')                           # bytes to ascii str
print(c)
