ingredient_list = []
naive_ingredient_list = []
allergen_dict = {}
for line in open("data/input_for_day21.txt", "r"):
    rough_ingredients, rough_allergens = line.rstrip().split("(contains ")
    ingredients = rough_ingredients.split(" ")[:-1]
    naive_ingredient_list.extend(ingredients)
    for ingredient in ingredients:
        if ingredient not in ingredient_list:
            ingredient_list.append(ingredient)
    allergens = rough_allergens.strip(")").split(", ")
    for elt in allergens:
        # for allergen in current line, we know the ingredient must be in the line
        if elt not in allergen_dict:
            allergen_dict[elt] = ingredients
        else:
            # current options for that allergen
            ingredient_possibilities = allergen_dict[elt].copy()
            for ingredient in allergen_dict[elt]:
                if ingredient not in ingredients:
                    # if it's not in the current line, can't be responsible for allergen
                    ingredient_possibilities.remove(ingredient)
            allergen_dict[elt] = ingredient_possibilities

allergic_ingredients = allergen_dict.values()
allergic = []
for allergic_ingredients_list in allergic_ingredients:
    allergic.extend(allergic_ingredients_list)
for key, value in allergen_dict.items():
    print(key, value)

safe = []
for ingredient in ingredient_list:
    if ingredient not in allergic:
        safe.append(ingredient)
occurrences = 0
for elt in naive_ingredient_list:
    if elt in safe:
        occurrences += 1
print(occurrences)

while not all([len(options) == 1 for keys, options in allergen_dict.items()]):
    for allergen, allergen_options in allergen_dict.items():
        if len(allergen_options) == 1:
            for other_allergen, other_options in allergen_dict.items():
                ingredient = allergen_options[0]
                if other_allergen !=  allergen and ingredient in other_options:
                    other_options.remove(allergen_options[0])
resstring = ""
for allergen in sorted(allergen_dict):
    resstring += str(allergen_dict[allergen][0]+",")
print(resstring[:-1])

