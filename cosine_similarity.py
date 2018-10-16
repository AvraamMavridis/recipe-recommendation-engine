import csv
import numpy
import copy
from collections import Counter
from scipy import spatial
from sklearn import metrics 

cosine_similarity_threshold = 0.2

# Flattens an array
def flat(arr):
  return filter(lambda x: x, [y for x in arr for y in x])

#
# Pick specific fields, and convert the
# values into an array of properties
#
def get_recipe_attributes(recipe):
  l = map(lambda x: x.split(','), [
    recipe['calories'], 
    recipe['protein'], 
    recipe['fat'], 
    recipe['sodium']
  ])
  return flat(l)

#
# Create a dictionary of attributes
#
def dictionary(arr):
  arr = numpy.unique(flat(arr))
  count = 0
  d = {} #Empty dictionary to add values into

  for i in arr:
    d[i] = count
    count+=1

  return d


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
  filtered = filter(lambda p: p, reader)

  r = []

  for row1 in filtered:
    r.append(get_recipe_attributes(row1))

  dict = dictionary(r)

  for rec1 in filtered:
    attrs1 = map_attrs_to_ints(rec1, dict)
    similar_recipes = []
    for rec2 in filtered:
      attrs2 = map_attrs_to_ints(rec2, dict)
      [attrs1, attrs2] = buildVector(attrs1, attrs2)
      cosine_similarity = 1 - spatial.distance.cosine(attrs1, attrs2)

      if(cosine_similarity > cosine_similarity_threshold and rec1['title'] != rec2['title']):
        copyRec = copy.deepcopy(rec2)
        copyRec['cosine_similarity'] = cosine_similarity
        similar_recipes.append(copyRec)
