from logger import logger_simple, parametrized_logger

if __name__ == '__main__':
    @logger_simple
    def get_data(file_name):
        cook_book = {}
        with open(file_name) as file:
            for line in file:
                ingredients = []
                cook_book[line.strip()] = ingredients
                dishes_quantity = int(file.readline().strip())
                for position in range(dishes_quantity):
                    consist = file.readline().strip().split('|')
                    custom_ingredients = {'ingredient_name': consist[0], 'quantity': consist[1], 'measure': consist[2]}
                    ingredients.append(custom_ingredients)
                file.readline()
        return cook_book


    @parametrized_logger('log_recipes')
    def get_shop_list_by_dishes(dishes, person_count):
        cook_book = get_data('recipes.txt')
        shop_list = {}
        for course in dishes:
            consist = cook_book.get(course)
            for ingredient in consist:
                if ingredient['ingredient_name'] not in shop_list:
                    quantity = int(ingredient['quantity']) * person_count
                    result = {'measure': ingredient['measure'], 'quantity': quantity}
                    shop_list[ingredient['ingredient_name']] = result
                else:
                    last_quantity = shop_list[ingredient['ingredient_name']]['quantity']
                    quantity = int(ingredient['quantity']) * person_count + last_quantity
                    result = {'measure': ingredient['measure'], 'quantity': quantity}
                    shop_list[ingredient['ingredient_name']] = result
        return print(shop_list)


    get_data('recipes.txt')

    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 5)
