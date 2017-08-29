def bad_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0

print(bad_function(11, 0))

mydict = {
    'lorie': 21,
    'derek': 24,
}

who = input('Who do you want to know their age? ')

try:
    age = mydict[who]
    print(who, 'is', age, 'years old')
except KeyError:
    print('I don\'t know her')
