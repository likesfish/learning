import random

name = []

names = ''
while names.lower() != "done":
    names = raw_input('What is your name? ')
    name.append(names)
name = name[0:-1]

number = raw_input('What size groups would you like? ')
group = int(number)

random.shuffle(name)
uhoh = len(name)
print '-----'
for names in range(0,uhoh,group):
    for i in range(names, group + names):
        print name[i]
    print '-----'
