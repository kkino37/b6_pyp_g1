res = map(lambda x: len(x), filter(lambda x: len(x) >= 4, ['julia', 'tom', 'carl', 'mary']))

res = [len(x) for x in ['julia', 'tom', 'carl', 'mary'] if len(x) >= 4]

print(res)


reduce(lambda acc, y: acc + y, [1, 2, 3, 4], 0)

acc = 0
for elem in [1,2,3,4]:
    acc = acc + elem
