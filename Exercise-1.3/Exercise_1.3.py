recipes_list = []
ingredients_list = []

def take_recipe():
  name = str(input('Name of recipe: '))
  cooking_time = int(input('Time to cook in minutes: '))
  ingredients = list(input('Neccessary ingredients (seperate each ingredient by a comma e.g., milk, sugar, cream): ').split(', '))
  recipe = {'name': name, 
            'cooking time (min)': cooking_time, 
            'ingredients': ingredients
            }
  return recipe

n = int(input('How many recipes would you like to add (please use a number e.g., 1, 2, or 3): '))

for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe['ingredients']:
    if ingredient not in ingredients_list:
      ingredients_list.append(ingredient)
  recipes_list.append(recipe)

for recipe in recipes_list:
  if recipe['cooking time (min)'] < 10 and len(recipe['ingredients']) < 4:
    recipe['difficulty'] = 'Easy'
  elif recipe['cooking time (min)'] < 10 and len(recipe['ingredients']) >= 4:
    recipe['difficulty'] = 'Medium'
  elif recipe['cooking time (min)'] >= 10 and len(recipe['ingredients']) < 4:
    recipe['difficulty'] = 'Intermediate'
  elif recipe['cooking time (min)'] >= 10 and len(recipe['ingredients']) >= 4:
    recipe['difficulty'] = 'Hard'

for recipe in recipes_list:
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

def all_ingredients():
  ingredients_list.sort()
  print('')
  print('=============================')
  print('All Ingredients: ')
  for ingredient in ingredients_list:
    print(ingredient)
  print('=============================')
  print('')

all_ingredients()