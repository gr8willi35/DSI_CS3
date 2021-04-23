# DSI Capstone 3
##Natural Language Processing on Book Summaries

For my final capstone project I am analyzing the wikipedia summaries for novels and determining if they should be labeled as "Science-Fiction" or not.

The dataset is the CMU Book Summary Dataset and the link to download is [here.](http://www.cs.cmu.edu/~dbamman/booksummaries.html "CMU Book Summary Dataset"

get corpus:
  *separate book summaries out into seperate documents
  *Lowercase the text
  *Tokenize

EDA:
  *Word Count Matrix

loop1:
  *Remove unwanted characters and punctuation
  *remove stop words

Vectorize bag of words (TFIDF and CountVectorizer)

loop2:
  *SnowBall stemming
  *expand stop words
  *Confusion Matrix
  
loop3:
  *Compute n-grams
   -less accurate
  *Create Roc Curve
  
test eventually against some wikipedia article
