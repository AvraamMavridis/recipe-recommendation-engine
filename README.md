# recipe-recommendation-engine

In this repo I am exploring the field of Recommendation Systems by building recommendation engines for Recipes based on different attributes and similarity metrics

## Content-based filtering

>Content-based filtering methods are based on a description of the item and a profile of the user’s preferences. In a content-based recommender system, keywords are used to describe the items and a user profile is built to indicate the type of item this user likes. In other words, these algorithms try to recommend items that are similar to those that a user liked in the past (or is examining in the present). [Wikipedia](https://en.wikipedia.org/wiki/Recommender_system)

>For example, if a user likes a web page with the words
“mobile”, “pen drive” and “RAM”, the CBF will recommend
pages related to the electronics world. Item description and a
profile of the user‟s orientation play an important role in
Content-based filtering. Content-based filtering algorithms
try to recommend items based on similarity count. The
best-matching items are recommended by comparing various
candidate items with items previously rated by the user.
A content based recommender works with data that the
user provides, either explicitly (rating) or implicitly (clicking
on a link). [Comparing Content Based and Collaborative
Filtering in Recommender Systems](https://www.ijntr.org/download_data/IJNTR03040022.pdf)

In our data we have many attributes that describe a recipe, for simplicity I picked 4 of these, `fat`, `sodium` `protein` and `calories`

```py
def get_recipe_attributes(recipe):
  return [
    recipe['fat'] or 0,
    recipe['protein'] or 0,
    recipe['calories'] or 0,
    recipe['sodium'] or 0
  ]
```

This returns a vector that we are using to caclulate the similarity between two recipes. To calculate the similarity we can use various similarity metrics, for example *Cosine Similarity*.

```bash
python cbf_cosine_similarity.py 'Garlic Baguette Crumbs '
```

## Cosine Similarity

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/1d94e5903f7936d3c131e040ef2c51b473dd071d "Cosine")




#### When to Use Cosine?
Cosine similarity is generally used as a metric for measuring distance when the magnitude of the vectors does not matter. This happens for example when working with text data represented by word counts. We could assume that when a word (e.g. `science`) occurs more frequent in document 1 than it does in document 2, that document 1 is more related to the topic of science. However, it could also be the case that we are working with documents of uneven lengths (Wikipedia articles for example). Then, `science` probably occurred more in document 1 just because it was way longer than document 2. Cosine similarity corrects for this.


### References

[Euclidean Vs Cosine](https://cmry.github.io/notes/euclidean-v-cosine)
