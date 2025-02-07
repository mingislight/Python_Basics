# List within the list []

menus = [['Egg Sandwich', 'Bagel', 'Coffee'],
         ['BLT', 'PB&J', 'Turkey Sandwich'],
         ['Soup', 'Salad', 'Spaghetti', 'Taco']]

print(menus[0][2]) # print the 1st list, the thrid item 


# List within the Dictionary

menus2 = {'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffee'],
         'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
         'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']}

for name, menu in menus2.items(): # print both key and value from dictionary.items()
    print(name, ":", menu)



# Dictionaries to Represent Objects
person = {'name': "Sarah Smith",
          'city': "Orlando",
          'age': '100'}

print(person.get('name'), 'is', person.get('age'), 'years old.')