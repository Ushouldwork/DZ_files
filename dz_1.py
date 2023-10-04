def read_recepies(filename):
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        line = file.readline().strip()
        while line:
            dish_name = line
            ingredients_count = int(file.readline().strip())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredient_info = file.readline().strip().split('|')
                ingredient_name = ingredient_info[0].strip()
                quantity = int(ingredient_info[1].strip())
                measure = ingredient_info[2].strip()
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients_list.append(ingredient)
            cook_book[dish_name] = ingredients_list
            line = file.readline().strip() 
    return cook_book

filename = 'recepies.txt' 
cook_book = read_recepies(filename)
print(cook_book)
