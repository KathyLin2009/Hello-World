import requests

def get_recipes(ingredients, api_key):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&number=5&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        recipes = response.json()
        return recipes
    else:
        print(f"Something went wrong!")
        return[]

def get_recipe_details(recipe_id, api_key):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        recipe_details = response.json()
        return recipe_details
    else:
        print(f"Something went wrong!")
        return None

api_key = "e7c981556a6e467c9450d5c4de4ccde7"
ingredients = input("Enter your ingredients (separate them with commas): ").split(',')
recipes = get_recipes(ingredients, api_key)
for i, recipe in enumerate(recipes):
    print(f"{i+1}. {recipe['title']}")
    print("  Recipe ID: ")
    print(recipe['id'])

recipe_num = input("Which recipe would you like to use? (Type the recipe ID, and None for none of them) ")
if(recipe_num == "None"):
    print("Okay!")
else:
    recipe_details = get_recipe_details(recipe_num, api_key)
    if recipe_details:
        print(f"Title: {recipe_details['title']}")
        print("Ingredients:")
        for ingredient in recipe_details['extendedIngredients']:
            print(f" - {ingredient['original']}")
        print("Instructions:")
        if recipe_details['instructions']:
            print(recipe_details['instructions'])
        else:
            print("Sorry! There are no instructions.")
    else:
        print("Something went wrong.")
