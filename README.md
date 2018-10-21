# recipe-recommendation-engine

In this repo I am exploring the field of Recommendation Systems by building recommendation engines for Recipes based on different attributes and similarity metrics

# Intro

## The `Long Tail` Phenomenon

In retail there is a well know phenomenon called `Long Tail`, 80% of the customers tend to buy 20% of the possible products, this leads to physicall stores to prefer having only these 20% popular products on the shelf. It's called long-tail distribiution because the most popular items are at the thickest end and the many not-so-popular ones stretching the tail out to its length. The items in the long tail are rare, obscure items, they are not very popular. 

Unlike with the physical stores, internet companies do not have to care about shelf space, they can offer millions of products. The problem is on how to present these niche products to the customer. Helping the user's discover these items in the long tail can return huge income to the vendors, so effective discovery is very critical.


![alt text](https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/figures/long_tail_problem.jpg?raw=true "Long Tail")


###### Refererences on long tail problem

- [Managing the "Long Tail" problem in Distribution and Retail
](https://www.youtube.com/watch?v=j58ML1TVSKw)
- [Long Tail - Wikipedia](https://en.wikipedia.org/wiki/Long_tail)

## The `Paradox of Choice`

In 2004, American psychologist Barry Schwartz, released a book called `The Paradox of Choice`, Barry in his book argues that having many options to choose from, in any particular situation, instead of producing feelings of abundance, too much choice overwhelms our already-exhausted brains.

<img src="https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/figures/paradox_of_choice.jpg?raw=true" height="350" />

_“The fact that some choice is good doesn’t necessarily mean that more choice is
better. As I will demonstrate, there is a cost to having an overload of choice. As a
culture, we are enamored of freedom, self-determination, and variety, and we are
reluctant to give up any of our options. But clinging tenaciously to all the choices
available to us contributes to bad decisions, to anxiety, stress, and dissatisfaction—
even to clinical depression.”_

<img src="https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/figures/paradox_cartoon.gif?raw=true" height="250" />


###### Refererences on the paradox of choice

- [Barry Schwartz  - The paradox of choice](https://www.ted.com/talks/barry_schwartz_on_the_paradox_of_choice?language=en)
- [Why too many choices is stressing us out? - Guardian](https://www.theguardian.com/lifeandstyle/2015/oct/21/choice-stressing-us-out-dating-partners-monopolies)

## Recommender Systems

So from one hand we have the long tail phenomenon, and the goal of companies to offer more and more products, from the other hand we have the Paradox of Choice, the customers try to find the best possible choice that will bring them joy and satisfaction.

The goal of a Recommender Systems, should be exactly this, to help the customer to discover the best possible option for their needs. With the term `recommender system` we are referring to a system that's capable of predicting the preference of a user for a set of available items. 

There are two main approaches on Recommender systems, `collaborative filtering` and `content-based filtering`. `Collaborative filtering` builds a model based on user's past interaction/behavior as well as similar decisions made by other users. Content-based filtering uses characteristics of an item in order to recommend items with similar characteristics. These approaches are often combined (Hybrid Recommender Systems).


### Collaborative filtering

>Collaborative filtering methods are based on collecting and analyzing a large amount of information on users’ behaviors, activities or preferences and predicting what users will like based on their similarity to other users. A key advantage of the collaborative filtering approach is that it does not rely on machine analyzable content and therefore it is capable of accurately recommending complex items such as movies without requiring an "understanding" of the item itself. 

For my examples, I will use a [csv file](https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/user_ratings.csv) that has 30 users and and their ratings on 30 recipes. The ratings are on a `1 to 5` scale, while `0` means that the user haven't try the recipe.

<img src="https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/figures/csv_users.png" />


#### Jaccard Similarity Coefficient

>The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size of the intersection divided by the size of the union 

`Jaccard Index = (the number in both sets) / (the number in either set)`


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Intersection_of_sets_A_and_B.svg/400px-Intersection_of_sets_A_and_B.svg.png" height="100" />

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Union_of_sets_A_and_B.svg/400px-Union_of_sets_A_and_B.svg.png" height="100" />

The mathimatical representation of it:

<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/eaef5aa86949f49e7dc6b9c8c3dd8b233332c9e7" />

To calculate the Jaccard Similarity we can take two approaches, either we can calculate the union and the intersection of the recipes they have tried ignoring their rating, or we can take the union of the recipes they rate exactly the same and the intersection of the recipes where they gave different rating.

For the 1st case, to calculuate the Jaccard Similarity between two users, we need to do some preprocessing, if a user has rate a recipe, means they try it, so we assigned `1`, otherwise we append `0` to our normalized vector.

```python
def normalize_vector(attrs):
  vector = []
  for val in attrs:
    if val == '0':
      vector.append(0)
    else:
      vector.append(1)
  return vector
```

e.g. `[0,4,5,1,0,3] -> [0,1,1,1,0,1]`

We can call the script passing the user for whom we want to find similar users.

```cmd
python clf_jaccard_normalized.py "Michael Grant"
```

This will give us:

<img src="https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/figures/jaccard_1.png?raw=true" />

So, `Scott Lane` is the user that is most similar to `Michael Grant`, so we can recommend to `Michael` the recipes that `Scott` have tried, but he hasn't. There is a problem though, if we look carefully the data we will see that these 2 users, although they tried the same recipes, they have completely different taste, whatever `Michael` rated as 5 or 4, `Scott` rated it as 1, and the other way around.

<img src="https://github.com/AvraamMavridis/recipe-recommendation-engine/blob/master/figures/michael_scott.png?raw=true" />

### Content-based filtering

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

In our data we have many attributes that describe a recipe, we use all of them except `title` and `rating`

```py
def get_recipe_attributes(recipe):
  keys = filter(lambda key: key != 'title' and key != 'rating', recipe.keys())
  return map(lambda x: recipe[x] or 0, keys)
```

This returns a vector that we are using to caclulate the similarity between two recipes. To calculate the similarity we can use various similarity metrics, for example *Cosine Similarity*.

```bash
python cbf_cosine_similarity.py 'Garlic Baguette Crumbs '
```
![alt text](https://raw.githubusercontent.com/AvraamMavridis/recipe-recommendation-engine/master/figures/cbf_cosine_similarity.png "Recipes Cosine")

## Cosine Similarity

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/1d94e5903f7936d3c131e040ef2c51b473dd071d "Cosine")


#### When to Use Cosine?
Cosine similarity is generally used as a metric for measuring distance when the magnitude of the vectors does not matter. This happens for example when working with text data represented by word counts. We could assume that when a word (e.g. `science`) occurs more frequent in document 1 than it does in document 2, that document 1 is more related to the topic of science. However, it could also be the case that we are working with documents of uneven lengths (Wikipedia articles for example). Then, `science` probably occurred more in document 1 just because it was way longer than document 2. Cosine similarity corrects for this.


### References

[Euclidean Vs Cosine](https://cmry.github.io/notes/euclidean-v-cosine)
