import random

name = []

names = ''
while names.lower() != "done":
    names = raw_input('What is your name? ')
    name.append(names)
name = name[0:-1]
print name

random.shuffle(name)
uhoh = len(name)
for names in range(0,uhoh,2):
    print name[names],name[names+1]
