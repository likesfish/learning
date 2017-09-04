from product import Product

inventory  = []
dictionary = {}

while True:
    item = raw_input('What item do you have? ')
    if item == 'done' or item == '':
        break
    number_item = raw_input('How many do you have? ')
    number_item = int(number_item)
    dictionary[item] = Product(item, quantity=number_item)
print dictionary

while True:
    first_question = raw_input('What would you like to buy? ')
    if first_question in dictionary:
        product = dictionary[first_question]
        print 'we have: ', product.quantity , product.name + 's'
    else:
        print "I'm sorry we don't have that"
        continue
    second_question = raw_input('How many would you like? ')
    second_question = int(second_question)


    try:
        product.sell(second_question)
    except Exception as e:
        print 'We don\'t have that many, or don\'t have any in stock'
        print 'but we have', product.quantity
