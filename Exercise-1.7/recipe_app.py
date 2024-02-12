from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

# Database connection object
engine = create_engine("mysql://cf-python:Mooseyman01@localhost/my_database")

# The Base class contains the properties from SQLAlchemy’s ORM system to create our table
Base = declarative_base()

# This is the blueprint for our Recipe class
class Recipe(Base):

    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + '-' + self.name + '-' + self.difficulty + ">"
    
    def __str__(self):
        output = '\nName: ' + str(self.name) + \
            "\nCooking time (minutes): " + str(self.cooking_time) + \
            "\nDifficulty: " + str(self.difficulty) + \
            "\nIngredients: " + str(self.ingredients)
        return output
    
    def calc_difficulty(self):

        ingredients_list = [self.ingredients.split(', ')]

        if (self.cooking_time < 10) and (len(ingredients_list) < 4):
            return 'Easy'
        elif (self.cooking_time < 10) and (len(ingredients_list) >= 4):
            return 'Medium'
        elif (self.cooking_time >= 10) and (len(ingredients_list) < 4):
            return 'Intermediate'
        elif (self.cooking_time >= 10) and (len(ingredients_list) >= 4):
            return 'Hard'
        else:
            print('error')    

# Creates tables of all the models that you’ve defined
Base.metadata.create_all(engine)

# Session lets you add entries to your table as objects
Session = sessionmaker(bind=engine)
session = Session()

# ====================================================================================

# Displays all the possible options for this program

def menu():

    choice = ''
    while (choice != 'quit'): 
        print('\nChose from the options below:')
        print('=============================\n')
        print('1. Create a new recipe')
        print('2. View all recipes')
        print('3. Search for a recipe by ingredient')
        print('4. Update an existing recipe')
        print('5. Delete a recipe')
        print('\nType "quit" to exit the program')
        choice = input('\nInput your option: ')

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            print('\nExiting...')
            session.close()
            engine.dispose()

# ====================================================================================

# Allows a user to create a new recipe which then gets added to our database
            
def create_recipe():

    ingredients = []

    name = input('\nEnter the name of the recipe: ')
    if len(name) > 50 or not name.isalnum():
        print('\nInvalid recipe name.')
        return

    cooking_time = input('Enter the cooking time (in minutes): ')
    if not cooking_time.isnumeric():
        print('\nInvalid cooking time.')
        return
    
    ingredients_num = input('Enter the number of ingredients you want to add: ')

    for _ in range(int(ingredients_num)):
        ingredient = input('Enter an ingredient: ')
        ingredients.append(ingredient)
    
    ingredients_str = ', '.join(ingredients)
    recipe = Recipe(name=name, ingredients=ingredients_str, cooking_time=int(cooking_time))
    recipe.difficulty = recipe.calc_difficulty()
    session.add(recipe)
    session.commit()
    print('\nRecipe added successfully.')

# ====================================================================================

# Allows the user the view all the attributes from recipes in our database
    
def view_all_recipes():

    recipes = session.query(Recipe).all()

    if not recipes:
        print('\nNo recipes available')
        return

    for recipe in recipes:
        print(recipe)

# ====================================================================================

# Allows the user to select an ingredient which then displays recipes containing that ingredient
        
def search_by_ingredients():

    all_ingredients = set()

    results = session.query(Recipe.ingredients).distinct().all()
    
    for (ingredients_str,) in results:
        all_ingredients.update(ingredients_str.split(', '))

    if session.query(Recipe.ingredients).count() == 0:
        print('\nNo ingredients found')
        return

    for num, ingredient in enumerate(all_ingredients, 1):
        print(f"{num}. {ingredient}")

    ingredient_numbers = input('\nEnter the numbers of the ingredients you want to search for (separated by spaces): \n')
    ingredient_split = ingredient_numbers.split(' ')
    search_ingredients  = [
        list(all_ingredients)[int(num) - 1]
        for num in ingredient_split
    ]

    conditions = []
    for ingredient in search_ingredients:
        like_term = "%" + ingredient + "%"
        condition = Recipe.ingredients.like(like_term)
        conditions.append(condition)

    recipes = session.query(Recipe).filter(*conditions).all()

    for recipe in recipes:
        print(recipe)

# ====================================================================================

# Allows the user to select a column to make an update too and then input the new value
        
def edit_recipe():

    print('')

    if session.query(Recipe.name).count() == 0:
        print('No recipes found')
        return

    results = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")

    recipe_id = input('\nEnter the ID of the recipe you want to edit: ')
    if not recipe_id.isdigit():
        print('Invalid ID. Please enter a number.')
        return

    recipe = session.query(Recipe).get(int(recipe_id))
    if not recipe:
        print('\nRecipe not found.')
        return

    print('\n1. Name\n2. Ingredients\n3. Cooking Time')

    column = input('\nEnter the number of the column you want to edit: ')

    if column == '1':
        new_name = input('\nEnter the new name: ')
        if len(new_name) > 50 or not new_name.isalnum():
            print('\nInvalid recipe name.')
            return
        
        recipe.name = new_name

    elif column == '2':
        new_ingredients = input('\nEnter the new ingredients (separated by a comma): ')
        recipe.ingredients = new_ingredients

    elif column == '3':
        new_cooking_time = input('\nEnter the new cooking time (in minutes): ')
        if not new_cooking_time.isnumeric():
            print('\nInvalid cooking time.')
            return
        
        recipe.cooking_time = int(new_cooking_time)

    recipe.difficulty = recipe.calc_difficulty()
    session.commit()

    print('\nRecipe updated successfully.')

# ====================================================================================

# Allows the user to select a recipe from the database to delete
    
def delete_recipe():

    if session.query(Recipe.name).count() == 0:
        print('\nNo recipes found')
        return
    
    recipes = session.query(Recipe.id, Recipe.name).all()
    for recipe_id, recipe_name in recipes:
        print(f"\n{recipe_id}. {recipe_name}")

    recipe_id = input('\nEnter the ID of the recipe you want to delete: ')
    if not recipe_id.isdigit():
        print('\nInvalid ID. Please enter a number.')
        return

    recipe = session.query(Recipe).get(int(recipe_id))
    if not recipe:
        print('\nRecipe not found.')
        return

    confirmation = input('\nAre you sure you want to delete this recipe? (y/n): ')
    if confirmation.lower() == 'y':
        session.delete(recipe)
        session.commit()
        print('\nRecipe deleted successfully.')
    else:
        menu()
    
# ====================================================================================

menu()