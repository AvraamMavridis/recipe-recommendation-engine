# recipe-recommendation-engine

In this repo I am exploring the field of Recommendation Systems by building recommendation engines for Recipes based on different attributes and similarity metrics

## Cosine Similarity


#### When to Use Cosine?
Cosine similarity is generally used as a metric for measuring distance when the magnitude of the vectors does not matter. This happens for example when working with text data represented by word counts. We could assume that when a word (e.g. `science`) occurs more frequent in document 1 than it does in document 2, that document 1 is more related to the topic of science. However, it could also be the case that we are working with documents of uneven lengths (Wikipedia articles for example). Then, `science` probably occurred more in document 1 just because it was way longer than document 2. Cosine similarity corrects for this.


### References

[Euclidean Vs Cosine](https://cmry.github.io/notes/euclidean-v-cosine)
