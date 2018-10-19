import csv
import random
from faker import Faker

fake = Faker()

NUMBER_OF_USERS = 30
NUMBER_OF_RECIPES = 30

with open('epi_r.csv') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter=',')
  filtered = map(lambda p: p['title'], reader)[0:NUMBER_OF_RECIPES]

  rows = ['user'] + filtered

  with open('user_ratings.csv', 'w') as fw:
    writer = csv.writer(fw, delimiter=',')
    writer.writerow(rows)

    for x in range(NUMBER_OF_USERS):
      name = fake.name()
      new_row = [name]

      for rec in range(NUMBER_OF_RECIPES):
        rating = random.randint(0,5)
        new_row.append(rating)

      writer.writerow(new_row)

    fw.close()
