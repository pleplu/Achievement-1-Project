class ShoppingList(object):
  def __init__(self, list_name):
    shopping_list = []
    self.list_name = list_name
    self.shopping_list = shopping_list
  
  def add_item(self, item):
    if item not in self.shopping_list:
      self.shopping_list.append(item)
      print('Item added to list')
    else: 
      print('error')

  def remove_item(self, item):
    try:
      self.shopping_list.remove(item)
    except:
      print('error')

  def view_list(self):
    print("\nItems in " + str(self.list_name) + '\n' + 30*'-')
    for item in self.shopping_list:
      print(' - ' + str(item))

pet_store_list = ShoppingList("Pet Store Shopping List")

pet_store_list.add_item('dog food')
pet_store_list.add_item('frisbee')
pet_store_list.add_item('bowl')
pet_store_list.add_item('collars')
pet_store_list.add_item('flea collars')

pet_store_list.remove_item('flea collars')

pet_store_list.add_item('frisbee')

pet_store_list.view_list()
      
# Output:
      
# Item added to list
# Item added to list
# Item added to list
# Item added to list
# Item added to list
# error

# Items in Pet Store Shopping List
# ------------------------------
#  - dog food
#  - frisbee
#  - bowl
#  - collars