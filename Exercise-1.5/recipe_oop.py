class Recipe(object):

    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        output = str(self.name)
        return output

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def get_cooking_time(self):
        output = int(self.cooking_time)
        return output

    def add_ingredients(self, *args):
        self.ingredients = args
        self.update_all_ingredients()

    def get_ingredients(self):
        print('\nIngredients in ' + self.name + ': ' )
        print('=====================')
        for ingredient in self.ingredients:
            print('- ' + str(ingredient))

    def calc_difficulty(self, cooking_time, ingredients):
        if (cooking_time < 10) and (len(ingredients) < 4):
            self.difficulty = 'Easy'
        elif (cooking_time < 10) and (len(ingredients) >= 4):
            self.difficulty = 'Medium'
        elif (cooking_time >= 10) and (len(ingredients) < 4):
            self.difficulty = 'Intermediate'
        elif (cooking_time >= 10) and (len(ingredients) >= 4):
            self.difficulty = 'Hard'
        else:
            print('error')
        return self.difficulty

    def get_difficulty(self):
        difficulty = self.calc_difficulty(self.cooking_time, self.ingredients)
        output = 'Difficulty: ' + str(self.cooking_time)
        self.difficulty = difficulty
        return output
    
    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def __str__(self):
        output = '\n=====================' + \
            '\nName: ' + str(self.name) + \
            '\nCooking Time (minutes): ' + str(self.cooking_time) + \
            '\nDifficulty: ' + str(self.difficulty) + \
            '\nIngredients: ' + str(self.ingredients) + \
            '\n====================='
        return output

recipes_list = []

def recipe_search(data, search_term):
    data = recipes_list
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


tea = Recipe("Tea")
tea.add_ingredients('Tea Leaves', 'Sugar', 'Water')
tea.set_cooking_time(5)
tea.get_difficulty()

recipes_list.append(tea)

coffee = Recipe('Coffee')
coffee.add_ingredients('Coffee Powder', 'Sugar', 'Water')
coffee.set_cooking_time(5)
coffee.get_difficulty()

recipes_list.append(coffee)

cake = Recipe('Cake')
cake.add_ingredients('Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk')
cake.set_cooking_time(50)
cake.get_difficulty()

recipes_list.append(cake)

bannana_smoothie = Recipe('Banana Smoothie')
bannana_smoothie.add_ingredients('Bananas', 'Milk', 'Peanut' 'Butter', 'Sugar', 'Ice Cubes')
bannana_smoothie.set_cooking_time(5)
bannana_smoothie.get_difficulty()

recipes_list.append(bannana_smoothie)

for recipe in recipes_list:
    print(recipe)

print('\nResults for "Water"')
print('=====================')
recipe_search(recipes_list, 'Water')

print('\nResults for "Sugar"')
print('=====================')
recipe_search(recipes_list, 'Sugar')

print('\nResults for "Bananas"')
print('=====================')
recipe_search(recipes_list, 'Bananas')

tea.get_ingredients()