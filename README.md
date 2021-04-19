# DSI_CS3
##Natural Language Processing on Book Summaries

Predict the genre of a book based on text. sci-fi or not sci-fi


get corpus:
  ..*separate book summaries out into seperate documents
  ..*Lowercase the text
  ..*Tokenize

EDA:
  ..*Word Count

loop1:
  ..*Remove unwanted characters and punctuation
  ..*remove stop words

Vectorize bag of words (TFIDF and CountVectorizer)

loop2:
  ..*stemming and lemmatizing
  ..*expand stop words
  ..*Confusion Matrix
  
loop3:
  ..*Compute n-grams
  ..*update roc curve
  ..*Create Roc Curve
  
test eventually against some wikipedia article
