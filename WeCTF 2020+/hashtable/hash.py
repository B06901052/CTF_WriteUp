if __name__ == "__main__":
    a = 3554082463
    b = 3568539197
    d = {}
    for x in range(4096, 1048577):
        h = pow(x, a, b) % 10000
        if not d.get(h):
            d[h] = [x]
        else:
            d[h].append(x)

    for x in d:
        if len(d[x]) >= 10:
            print(d[x])