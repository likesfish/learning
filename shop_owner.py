inventory  = []
dictionary = {}

while True:
    item = raw_input('What item do you have? ')
    if item == 'done' or item == '':
        break
    number_item = raw_input('How many do you have? ')
    number_item = int(number_item)
    dictionary[item] = number_item
print dictionary

while True:
    first_question = raw_input('What would you like to buy? ')
    if first_question in dictionary:
        print 'we have: ', dictionary[first_question]
    else:
        print "I'm sorry we don't have that"
        continue
    second_question = raw_input('How many would you like? ')
    second_question = int(second_question)

    #how many we will have = have
    have = dictionary[first_question] - second_question

    if have >= 0:
        print 'after you make this purchase we will have: ', have
        dictionary[first_question] = have
    else:
        print 'We don\'t have that many, or don\'t have any in stock'
        print 'but we have', dictionary[first_question]
