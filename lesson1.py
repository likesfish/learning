infile = open('groups.txt').read().strip('\n')
groups = infile.split('\n\n')

for i, group in enumerate(groups):
    groups[i] = group.split('\n')
print(groups)
