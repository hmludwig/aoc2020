import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()
data = [x.split('(contains ') for x in data]
data = [(sorted(x.split()), y.replace(')', '').replace(',', '').split())
        for x, y in data]

allergen_wiki = {}
all_ingredients = []
for foods, allergens in data:
    all_ingredients.extend(foods)
    for allergen in allergens:
        if allergen in allergen_wiki:
            allergen_wiki[allergen].intersection_update(set(foods))
        else:
            allergen_wiki[allergen] = set(foods)

tmp = []
for key in allergen_wiki:
    tmp.append(allergen_wiki[key])
known_ingredients = set.union(*tmp)

solution1 = 0
for x in all_ingredients:
    if x not in known_ingredients:
        solution1 += 1

print(f'Part 1: {solution1}')

while sum([len(x) for x in allergen_wiki.values()]) != len(allergen_wiki):
    allergen_wiki = dict(sorted(allergen_wiki.items(), key = lambda x : len(x[1])))
    for key1 in allergen_wiki:
        if len(allergen_wiki[key1]) == 1:
            for key2 in allergen_wiki:
                if key1 != key2:
                    allergen_wiki[key2] -=  allergen_wiki[key1]

solution2 = ''
for key in sorted(allergen_wiki):
    solution2 += str(list(allergen_wiki[key])[0]) + ','

print(f'Part 2: {solution2[:-1]}')
