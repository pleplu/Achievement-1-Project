import pickle

def display_recipe(recipe):
  print('')
  print('=============================')
  print('Recipe: ', recipe['name'])
  print('Cooking time (min): ', recipe['cooking time (min)'])
  print('Ingredients: ')
  for ingredient in recipe['ingredients']:
    print(ingredient)
  print('Difficulty: ', recipe['difficulty'])
  print('=============================')
  print('')

def search_ingredient(data):
  available_ingredients = enumerate(data['all_ingredients'])
  ingredient_list = list(available_ingredients)

  print('Ingredients List: ')

  for ingredient in ingredient_list:
    print(ingredient[0], ingredient[1])
  try:
    number = int(input('Enter the number for ingredents you would like to search: '))
    ingredient_searched = ingredient_list[number][1]
  except:
    print('The number you entered is incorrect.')
  else:
    for recipe in data['recipes_list']:
      if ingredient_searched in recipe['ingredients']:
        display_recipe(recipe)

filename = input('Enter the filename where you\'ve stored your recipes: ')

try:
    file = open(filename, "rb")
    data = pickle.load(file)
except FileNotFoundError:
    print('Incorrect file.')
except:
    print('An unexpected error has occurred.')
else:
    file.close()
    search_ingredient(data)