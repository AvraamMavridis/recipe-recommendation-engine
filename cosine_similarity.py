import csv
import numpy
import copy
from collections import Counter
from scipy import spatial
from sklearn import metrics 
import plot_results as plt
import sys

recipe_to_look = sys.argv[1]
cosine_similarity_threshold = 0.2

# Flattens an array
def flat(arr):
  return filter(lambda x: x, [y for x in arr for y in x])

#
# Pick specific fields, and convert the
# values into an array of properties
#
def get_recipe_attributes(recipe):
  # keys = filter(lambda key: key != 'title' and key != 'rating', recipe.keys())
  # return map(lambda x: recipe[x] or 0, keys)
  return [
    recipe['fat'] or 0,
    recipe['protein'] or 0,
    recipe['calories'] or 0,
    recipe['sodium'] or 0
  ]


def buildVector(iterable1, iterable2):
    iterable1.sort()
    iterable2.sort()
    counter1 = Counter(iterable1)
    counter2= Counter(iterable2)
    all_items = set(counter1.keys()).union( set(counter2.keys()) )
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2


def map_attrs_to_ints(recipe, dict):
  return map(lambda x: dict[x], get_recipe_attributes(recipe))


with open('epi_r.csv') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter=',')
  filtered = filter(lambda p: p, reader)[0:200]
  recipe_to_look = filter(lambda p: p['title'] == recipe_to_look, filtered)[0]

  attrs = map(lambda x: float(x), get_recipe_attributes(recipe_to_look))

  similar_recipes = []
  for rec2 in filtered:
    attrs2 = map(lambda x: float(x), get_recipe_attributes(rec2))
    [attrs, attrs2] = buildVector(attrs, attrs2)
    print(attrs, attrs2)
    cosine_similarity = 1 - spatial.distance.cosine(attrs, attrs2)

    if(cosine_similarity > cosine_similarity_threshold and recipe_to_look['title'] != rec2['title']):
      rec2['cosine_similarity'] = cosine_similarity
      similar_recipes.append(rec2)

  similar_recipes = sorted(similar_recipes, key=lambda x: x['cosine_similarity'])

  plt.draw(similar_recipes, 'cosine_similarity', recipe_to_look['title'])
