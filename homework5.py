import random

names = []

name = ''
while True:
    name = raw_input('What is your names? ')
    if name == 'done':
        break
    names.append(name)

number = raw_input('What size groups would you like? ')
group = int(number)

random.shuffle(names)

for name in range(0, len(names), group):
    for i in range(name, group + name):
        print names[i]
    print '-----'
