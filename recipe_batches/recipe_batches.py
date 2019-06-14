#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):            
    needed_ingredients = {key: ingredients[key] for key in ingredients if key in recipe}
    if list(needed_ingredients.keys()) != list(recipe.keys()):
        return 0

    batches = 1000
    for item in needed_ingredients:
        if ingredients[item] // recipe[item] < batches:
            batches = ingredients[item] // recipe[item]
    
    return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))