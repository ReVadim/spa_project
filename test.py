string = ['1', '3', '5', '6']
digit = '5'

a = [1, 2, 3, 5, 7]
b = 3

if b not in a:
    a.append(b)
    a.sort()

print(a.index(b))
