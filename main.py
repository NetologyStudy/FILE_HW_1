from pprint import pprint
file_name = 'recipes.txt'

def read_recipes(file):
    cook_book = {}
    with open(file, encoding='utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredient_count = int(f.readline().strip())

            ingredients = []
            for _ in range(ingredient_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingrdient = {'ingredient_name': ingredient_info[0],
                             'quantity': int(ingredient_info[1]),
                             'measure': ingredient_info[2]}
                ingredients.append(ingrdient)
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    person_dishes = {}
    ingredients_name = []
    for dish in dishes:
        ingredients = read_recipes(file_name)[dish]
        for ingredient in ingredients:
            ingredients_name.append(ingredient['ingredient_name'])
            person_dishes[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                            'quantity': ingredient['quantity'] * person_count}

    for person_dish in person_dishes:
        if ingredients_name.count(person_dish) > 1:
            person_dishes[person_dish]['quantity'] *= ingredients_name.count(person_dish)

    return person_dishes


def main():
    list_cook_book = list(read_recipes(file_name))
    list_dish = []
    while True:
        dish_name = input('Введите название блюда(Чтобы закончить нажмите "Enter"): ').capitalize()
        if dish_name in list_cook_book:
            list_dish.append(dish_name)
            print(f'Блюдо {dish_name} добавлено в список')
        elif not dish_name:
            if list_dish:
                print(f'Вы будете готовить {", ".join(list_dish)}')
                persons = int(input('Введите количество персон: '))
                pprint(get_shop_list_by_dishes(list_dish, persons))
            else:
                print('Вы ничего не выбрали')
            break

        else:
            print(f'Рецепта {dish_name} нет')


if __name__ == '__main__':
    main()


