import csv
from scipy.spatial import distance
import sys
import matplotlib.pyplot as plt
import numpy as np
import helpers

user = sys.argv[1]

def normalize_vector(attrs):
  vector = []
  for val in attrs:
    if val == '0':
      vector.append(0)
    else:
      vector.append(1)
  return vector


def draw(users, similarity_metric, title):
    names = list(map(lambda x: helpers.remove_non_ascii(x['user'][0:20]), users))
    similarities = list(map(lambda x: x[similarity_metric], users))

    index = np.arange(len(names))
    plt.rcParams['figure.figsize'] = (15,6)
    plt.bar(index, similarities)
    plt.xlabel('Users', fontsize=15)
    plt.ylabel('Similarity', fontsize=15)
    plt.ylim(min(similarities), max(similarities) + 0.1)
    plt.xticks(index, names, fontsize=7, rotation=90)
    plt.title(title)
    plt.subplots_adjust(bottom=0.28, left=0.1, right=0.98)
    plt.show()

with open('user_ratings.csv') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter=',')
  users = filter(lambda p: p, reader)

  user_to_look = filter(lambda p: p['user'] == user, users)[0]
  user_values_jac = normalize_vector(user_to_look.values()[:-1])

  for val in users:
    user2_values_jac = normalize_vector(val.values()[:-1])
    user_name = val.values()[-1]

    val['jaccard_similarity'] = 1 - distance.jaccard(user2_values_jac, user_values_jac)

  users = filter(lambda p: p['user'] != user_to_look['user'], users)
  users = sorted(users, key=lambda x: x['jaccard_similarity'])

  draw(users, 'jaccard_similarity', user_to_look['user'])
  
