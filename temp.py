def print_swap(x, y):
    temp = y
    x = y
    y = temp
    print('{}{}'.format(x,y))

print_swap(10, 20)
print_swap('창식', '정은')
