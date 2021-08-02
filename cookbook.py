# list of recipes
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
# inputting the ingredient
ingredient = input()
# recipe according ingredients
if ingredient in pasta:
    print("pasta time!")
if ingredient in apple_pie:
    print("apple pie time!")
if ingredient in ratatouille:
    print("ratatouille time!")
if ingredient in chocolate_cake:
    print("chocolate cake time!")
if ingredient in omelette:
    print("omelette time!")
# If the ingredient is featured in several recipes, all of them recipes are outputted in the order they're featured in the cook book.

