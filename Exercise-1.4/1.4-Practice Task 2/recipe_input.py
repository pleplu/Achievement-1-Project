import pickle

recipes_list = []
all_ingredients = []

def take_recipe():
  name = str(input('Name of recipe: '))
  cooking_time = int(input('Time to cook in minutes: '))
  ingredients = list(input('Neccessary ingredients (seperate each ingredient by a comma and a space e.g., milk, sugar, cream): ').split(', '))
  def calc_difficulty():
    if cooking_time < 10 and len(ingredients) < 4:
      difficulty = 'Easy'
    elif cooking_time < 10 and len(ingredients) >= 4:
      difficulty = 'Medium'
    elif cooking_time >= 10 and len(ingredients) < 4:
      difficulty = 'Intermediate'
    elif cooking_time >= 10 and len(ingredients) >= 4:
      difficulty = 'Hard'
    return difficulty
  difficulty = calc_difficulty()
  recipe = {'name': name, 
            'cooking time (min)': cooking_time, 
            'ingredients': ingredients,
            'difficulty': difficulty
            }
  return recipe

filename = input('Enter the filename where you want to store your recipes: ')

try:
  file = open(filename, 'br')
  data = pickle.load(file)
except FileNotFoundError:
  print('File does not exist, creating new file.')
  data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}
except:
  print('An unexpected error has occurred.')
  data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}
else:
  file.close()
finally:
  recipes_list = data['recipes_list']
  all_ingredients = data['all_ingredients']

n = int(input('How many recipes would you like to add (please use a number e.g., 1, 2, or 3): '))

for i in range(n):
  recipe = take_recipe()
  for ingredient in recipe['ingredients']:
    if ingredient not in all_ingredients:
      all_ingredients.append(ingredient)
  recipes_list.append(recipe)  

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

recipe_file = open(filename, 'wb')
pickle.dump(data, recipe_file)
recipe_file.close()
print('New recipe has been added to list.')