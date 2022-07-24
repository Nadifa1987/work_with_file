import os

FILE_NAME = "rspt.txt"
BASE_PATH = os.getcwd()
full_path = os.path.join(BASE_PATH, FILE_NAME)

def reader(full_path):
    with open(full_path, "r", encoding = "UTF-8") as file:
        cook_book = {}
        for line in file:
            meal = line.strip()
            ingredients = []
            for item in range(int(file.readline())):
                ingredient = file.readline()
                ind_new = ingredient.replace(" | ",",").strip()
                list = ind_new.split(',')
                keys_list = ('ingredient_name', 'quantity', 'measure')
                dict_for_ing = dict(zip(keys_list, list))
                ingredients.append(dict_for_ing)
                cook_book[meal] = ingredients
            file.readline()
        print(cook_book)


        def shop_list(meals, person):
            shop_list = {}
            for meal in meals:
                for key, value in cook_book.items():
                    if meal == key:
                        for product_dict in value:
                            ingredient = product_dict['ingredient_name']
                            if ingredient in shop_list.keys():
                                shop_list[ingredient]['quantity'] += (int(product_dict['quantity']) * person)
                            else:
                                amount = {'measure': product_dict['measure'], 'quantity': int(product_dict['quantity']) * person}
                                shop_list.setdefault(product_dict['ingredient_name'], amount)

            print(shop_list)

        shop_list(["Омлет", "Омлет", "Утка по-пекински","Фахитос", "Фахитос"], 8)

reader(full_path)