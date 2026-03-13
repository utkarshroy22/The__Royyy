# Creative Recipe Book using Nested Dictionary
recipes = {
    "Butter Chicken": {
        "ingredients": {"chicken": "500g", "butter": "50g", "cream": "200ml", "spices": ["garam masala", "cumin", "chili"]},
        "time": "45 min",
        "difficulty": "medium",
        "cuisine": "Indian"
    },
    "Pasta": {
        "ingredients": {"pasta": "300g", "tomato": "400g", "cheese": "100g", "spices": ["basil", "oregano"]},
        "time": "20 min",
        "difficulty": "easy",
        "cuisine": "Italian"
    },
    "Biryani": {
        "ingredients": {"rice": "400g", "chicken": "600g", "yogurt": "200g", "spices": ["saffron", "cardamom", "cloves"]},
        "time": "60 min",
        "difficulty": "hard",
        "cuisine": "Indian"
    }
}

print("Recipe Book:")
for dish, info in recipes.items():
    print(f"{dish}: {info['time']}, {info['difficulty']}, Cuisine: {info['cuisine']}")
    print(f"  Ingredients: {', '.join([f'{k}: {v}' for k,v in info['ingredients'].items()])}")
    print()

# Indian recipes filter
indian = {dish: info for dish, info in recipes.items() if info['cuisine'] == 'Indian'}
print("Indian Recipes:", indian)

# Average cooking time
times = [int(info['time'].split()[0]) for info in recipes.values()]
avg_time = sum(times) / len(times)
print(f"Average Cooking Time: {avg_time:.1f} min")

# Most common spice
all_spices = []
for info in recipes.values():
    all_spices.extend(info['ingredients'].get('spices', []))
spice_count = {}
for spice in all_spices:
    spice_count[spice] = spice_count.get(spice, 0) + 1

# Easy & quick recipes
easy_quick = {d: i for d, i in recipes.items() if i['difficulty'] == 'easy' and int(i['time'].split()[0]) < 30}
print("Easy & Quick:", easy_quick)