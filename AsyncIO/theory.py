def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd

g = odds(1, 10)

list = []

for i in g:
    list += g
    print(list)

print (g)