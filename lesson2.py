import random

name = ''
while name.lower() != "done":
    name = raw_input('What is your name? ')
    first_letter = name[0]
    print "The first letter of your name is {}!".format(first_letter)


compliment = ["you're cool", "nice name!", "buy me a drink"]
print random.choice(compliment)




#     print "the first letter is D"
# else:
#     print "that's a cool name"
#
# Fifth_letter = name[4]
# if Fifth_letter == "Q" or Fifth_letter == "q":
#     print "wtf"
# else:
#     print "seems okay"
