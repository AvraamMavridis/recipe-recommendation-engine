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

With the term `recommender system` we are referring to a system that's capable of predicting the preference a user for a set of available items. 


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
