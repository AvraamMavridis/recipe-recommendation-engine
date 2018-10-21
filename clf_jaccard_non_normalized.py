import csv
from scipy.spatial import distance
import sys
import matplotlib.pyplot as plt
import numpy as np
import helpers
from plot_results import draw_users

user = sys.argv[1]


with open('user_ratings.csv') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter=',')
  users = filter(lambda p: p, reader)

  user_to_look = filter(lambda p: p['user'] == user, users)[0]
  user_values_jac = map(lambda x: int(x), user_to_look.values()[:-1])

  for val in users:
    user2_values_jac = map(lambda x: int(x), val.values()[:-1])
    user_name = val.values()[-1]

    val['jaccard_similarity'] = 1 - distance.jaccard(user2_values_jac, user_values_jac)

  users = filter(lambda p: p['user'] != user_to_look['user'], users)
  users = sorted(users, key=lambda x: x['jaccard_similarity'])

  draw_users(users, 'jaccard_similarity', user_to_look['user'])
  
