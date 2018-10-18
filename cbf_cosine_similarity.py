import csv
import numpy
import copy
from collections import Counter
from scipy import spatial
from sklearn import metrics 
import plot_results as plt
import sys

recipe_to_look = sys.argv[1]
cosine_similarity_threshold = 0.1

# Flattens an array
def flat(arr):
  return filter(lambda x: x, [y for x in arr for y in x])

#
# Pick specific fields, and convert the
# values into an array of properties
#
def get_recipe_attributes(recipe):
  keys = filter(lambda key: key != 'title' and key != 'rating', recipe.keys())
  return map(lambda x: recipe[x] or 0, keys)

def normalize_vectors(attrs, attrs2):
  vector1 = []
  vector2 = []
  for idx, val in enumerate(attrs):
    # We skip the attributes for which both recipes have zero value
    if attrs2[idx] == 0 and val == 0:
      continue
    else:
      vector1.append(1)
      vector2.append(0)
      if(val == attrs2[idx]):
        vector2[-1] = 1
  return vector1, vector2


def map_attrs_to_ints(recipe, dict):
  return map(lambda x: dict[x], get_recipe_attributes(recipe))


with open('epi_r.csv') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter=',')
  filtered = filter(lambda p: p, reader)
  recipe_to_look = filter(lambda p: recipe_to_look in p['title'], filtered)[0]

  attrs = map(lambda x: float(x), get_recipe_attributes(recipe_to_look))

  similar_recipes = []
  for rec2 in filtered:
    attrs2 = map(lambda x: float(x), get_recipe_attributes(rec2))
    vc1, vc2 = normalize_vectors(attrs, attrs2)
    cosine_similarity = 1 - spatial.distance.cosine(vc1, vc2)

    if(cosine_similarity > cosine_similarity_threshold and recipe_to_look['title'] != rec2['title']):
      rec2['cosine_similarity'] = cosine_similarity
      # print(rec2['cosine_similarity'], rec2['title'], attrs, attrs2, vc1, vc2)
      similar_recipes.append(rec2)

  similar_recipes = sorted(similar_recipes, key=lambda x: x['cosine_similarity'])[:100]

  plt.draw(similar_recipes, 'cosine_similarity', recipe_to_look['title'])
