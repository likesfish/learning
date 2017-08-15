a = []
number = ''
while True:
    number = raw_input('Put in a value: ')
    if number == 'done':
        break
    len(number)
    a.append(number)
print (a)

def revlist(a):

    n = 0
    b = len(a)-1
    for number in a:
        if n < b/2:
            a[n], a[b-n] = a[b-n], a[n]
        else:
            break
        n = n + 1
    print (a)

revlist(a)
