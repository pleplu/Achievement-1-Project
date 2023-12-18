# Achievement-1-Project

Exercise-1.1 - https://github.com/pleplu/Achievement-1-Project/tree/main/Exercise-1.1

# Exercise-1.1

Step 1: Firstly verify you have the correct version of python installed (version 3.8.7).

https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/Documentation/python-version.png

If not, download the correct version of python here: https://www.python.org/downloads/release/python-387/

Step 2: Next, create a new virtual enviroment in your terminal using the command "mkvirtualenv cf-python-base", and verify it works using "workon cf-python-base".

https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/Documentation/workon-env.png

Step 3: Then create a script in the code editor of your choice that takes the sum of two variables.

Code: https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/add.py

https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/Documentation/add.png

Step 4: Install and verify that ipython works in your virtual enviroment by firstly using "install ipython", and then "ipython" in your terminal.

https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/Documentation/ipython-shell.png

Step 5: Export a requirements.txt file containing all the required packages to a new virtual enviroment. First use "pip freeze > requirements.txt" to create a file containing the packages, and then "pip install -r requirements.txt" in your new enviroment to download all the required packages. 

https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/Documentation/pip-freeze.png

https://github.com/pleplu/Achievement-1-Project/blob/main/Exercise-1.1/Documentation/install-requirements.png

# Exercise-1.2

Step 1: For the data structure for recipe_1 I decided to use a dictionary due to my use of key value pairs for each recipe. Also, say I wanted to add ingredients, or change certain parts of the recipe, I can simply update those values rather than remaking the entire recipe. 

Step 2: As for all_recipes I used a list to store recipe data. I've used a list for this purpose due to it being mutable and thus easier to store and modify data. 
