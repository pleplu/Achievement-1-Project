import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='cf-python', passwd='Mooseyman01')

cursor = conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS task_database')

cursor.execute('USE task_database')

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
ingredients VARCHAR(255),
cooking_time INT,
difficulty VARCHAR(20)
)''')

def menu(conn, cursor):

    choice = ''
    while (choice != 'quit'): 
        print('\n\nChose from the options below:')
        print('1. Create a new recipe')
        print('2. Search for recipe by ingredient')
        print('3. Update an existing recipe')
        print('4. Delete a recipe')
        print('Type "quit" to exit the program')
        choice = input('\nInput your option: ')

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)

# ====================================================================================

def create_recipe(conn, cursor):

    recipe_ingredients = []

    name = str(input('\nEnter the name of the recipe: '))
    cooking_time = int(input('Enter the cooking time (in minutes): '))
    ingredients = input('Enter the ingredients used (separated by a comma): ')
    recipe_ingredients.append(ingredients)
    difficulty = calc_difficulty(cooking_time, recipe_ingredients)

    ingredients_string = ', '.join(recipe_ingredients)

    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, ingredients_string, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print('\nRecipe added')

# ====================================================================================

def calc_difficulty(cooking_time, recipe_ingredients):

    if (cooking_time < 10) and (len(recipe_ingredients) < 4):
        difficulty = 'Easy'
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty = 'Medium'
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty = 'Intermediate'
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty = 'Hard'
    else:
        print('error')

    return difficulty

# ====================================================================================

def search_recipe(conn, cursor):

    cursor.execute('SELECT DISTINCT ingredients FROM Recipes')
    all_ingredients = set()

    for (ingredients,) in cursor:
        all_ingredients.update(ingredients.split(', '))

    print('\nIngredients: ')
    for ingredient in all_ingredients:
        print(ingredient)

    search_input = input('\nEnter the name of the ingredient to find matching recipes: ')
    query = 'SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE %s'
    search_ingredient = f'%{search_input}%'

    cursor.execute(query, (search_ingredient,))
    for name, ingredients, cooking_time, difficulty in cursor:
        print(f'\nRecipe: {name}, Ingredients: {ingredients}, Cooking Time: {cooking_time}, Difficulty: {difficulty}')

# ====================================================================================

def update_recipe(conn, cursor):

    all_recipes(conn, cursor) 
    recipe_update = int((input('\nPlease enter the ID of the recipe you want to update: ')))
    column_update = str(input('\nPlease enter the column you want to update ("name", "cooking_time", or "ingredients"): '))
    updated_value = input('\nEnter the new value: ')

    if column_update == 'name':
        cursor.execute('UPDATE Recipes SET name = %s WHERE id = %s', (updated_value, recipe_update))
        print('\nName updated')

    elif column_update == 'cooking_time':
        cursor.execute('UPDATE Recipes SET cooking_time = %s WHERE id = %s', (updated_value, recipe_update))
        cursor.execute('SELECT * FROM Recipes WHERE id = %s', (recipe_update, ))
        updated_recipe = cursor.fetchall()
        recipe_ingredients = tuple(updated_recipe[0][2].split(','))
        cooking_time = updated_recipe[0][3]
        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (updated_difficulty, recipe_update))
        print('\nCooking time updated')

    elif column_update == 'ingredients':
        cursor.execute('UPDATE Recipes SET ingredients = %s WHERE id = %s', (updated_value, recipe_update))
        cursor.execute('SELECT * FROM Recipes WHERE id = %s', (recipe_update, ))
        updated_recipe = cursor.fetchall()
        recipe_ingredients = tuple(updated_recipe[0][2].split(','))
        cooking_time = updated_recipe[0][3]
        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s', (updated_difficulty, recipe_update))
        print('\nIngredients updated')

    conn.commit()

# ====================================================================================

def delete_recipe(conn, cursor):

    all_recipes(conn, cursor)
    recipe_delete = ((input('\nEnter the ID of the recipe you want to delete: ')))
    cursor.execute('DELETE FROM Recipes WHERE id = %s',
                   (recipe_delete,))

    conn.commit()
    print('\nRecipe deleted')

# ====================================================================================

def all_recipes(conn, cursor):

    cursor.execute('SELECT * FROM Recipes')
    results = cursor.fetchall()

    for row in results:
        print('\nID: ', row[0])
        print('Name: ', row[1])
        print('Ingredients: ', row[2])
        print('Cooking Time: ', row[3])
        print('Difficulty: ', row[4])

menu(conn, cursor)