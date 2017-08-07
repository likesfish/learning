import random

names = []

name = ''
while True:
    name = input('What are your names? ')
    if name == 'done':
        break
    names.append(name)

number = input('What size groups would you like? ')
group_size = int(number)

def make_groups(names, group_size):

    random.shuffle(names)
    #boundary slices list into groups
    all_groups = []
    for boundary in range(0, len(names), group_size):
        group = []
        for i in range(boundary, boundary + group_size, 1):
            #i am appending the name [i] in the list of names
            if i >= len(names):
                break
            group.append(names[i])
        all_groups.append(group)
    return all_groups

print(make_groups(names, group_size))
