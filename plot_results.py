import matplotlib.pyplot as plt
import numpy as np
import helpers

def draw(recipes, similarity_metric, title):
    names = list(map(lambda x: helpers.remove_non_ascii(x['title'][0:20]), recipes))
    similarities = list(map(lambda x: x[similarity_metric], recipes))

    index = np.arange(len(names))
    plt.rcParams['figure.figsize'] = (15,6)
    plt.bar(index, similarities)
    plt.xlabel('Similar Recipes', fontsize=15)
    plt.ylabel('Similarity', fontsize=15)
    plt.ylim(min(similarities), max(similarities) + 0.1)
    plt.xticks(index, names, fontsize=7, rotation=90)
    plt.title(title)
    plt.subplots_adjust(bottom=0.28, left=0.1, right=0.98)
    plt.show()

def draw_users(users, similarity_metric, title):
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
