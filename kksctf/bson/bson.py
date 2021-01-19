from collections import Counter

key = 92
flag = [55, 55, 47, 39, 54, 47, 108, 50, 3, 53, 47, 3, 63, 108, 108, 48, 3, 62, 41, 40, 3, 52, 61, 42,
        111, 3, 37, 51, 41, 3, 40, 46, 53, 57, 56, 3, 49, 111, 47, 47, 28, 59, 57, 3, 44, 61, 63, 55, 33]

# freq. analysis
print(Counter(flag))

# bytewise xor
flag = [(b ^ key).to_bytes(1, 'big') for b in flag]
flag = b''.join(flag)
flag = flag.decode('ascii')
print(flag)
