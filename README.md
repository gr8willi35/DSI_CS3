# DSI Capstone 3
## Natural Language Processing Applied to Book Summaries.


For my final capstone project I am analyzing the wikipedia summaries for novels and determining if they should be categorized as "Science-Fiction" or not.

<img src="https://user-images.githubusercontent.com/25779351/116443332-28609880-a819-11eb-8c9f-a6a75a0f4341.jpg" width="260" height="344">

The dataset is the CMU Book Summary Dataset and the link to download is [here](http://www.cs.cmu.edu/~dbamman/booksummaries.html "CMU Book Summary Dataset").


The CMU dataset contains metadata including the author, title, genre and a body summary. My first step was to clean the data and create a column of targets for a model.  I am only interested in the genre and body because I want to focus on the contents of the summary to make a prediction, and I can use the genre data to create a new column of targets where the value is True (Sci-Fi) or False (not Sci-Fi)

Once the dataframe was organized I determined the genres were split at roughly 22.5% being science fiction and 77.5% not.

![Data_proportions](https://user-images.githubusercontent.com/25779351/116435335-db78c400-a810-11eb-8fce-1703b87faa24.png)


Next step in the process was to build a basic model. I performed a train-test-split (75% training data), and I chose to use the scikit learn random forest for my model. Using the default parameters I was able achieve an accuracy of 84%.



The most most important words are displayed in the following figure.

![body_scores](https://user-images.githubusercontent.com/25779351/116598461-785c5f80-a8ec-11eb-80f5-11e976039f70.png)


After looking at my most important words I decided I needed to add a stopword list and implement stemming. Stopwords removes words with no bearing on the context of the document and skew the accuracy of the model.  Words like "the", "of", "and" etc. are dumped and the model can get a better accuracy score.  Stemming is the process of getting the root of words to reduce frequency.  In the most important words figure the reader may notice variations of "human".  By getting to the root word we can reduce the corpus and get a better idea of what words have an impact.  Below you can see the effects of these changes to our most important words list.

![Final Important Words](https://user-images.githubusercontent.com/25779351/116606073-d0e42a80-a8f5-11eb-8475-7d578cb29623.png)





This brought me some improvements and the next step was to stem my words.  I was still having some issues with accuracy and expanded my stop word list, including words that had a really heavy weight to them that would skew the whole model.

After stemming my words I changed the depth and max feature parameters to improve the calculation.

I tried implementing n-grams but after a few attempts removed it as it reduced my overall accuracy and performance.  If there was more time it would be better to include bi-grams and then greatly expland my stopword list.

Lastly I looked to adjusting my threshold for acceptance to improve the model.  The default is .50 so I tried increasing it by .05 intervals comparing the results  and between .60 and .65 provided the best threshold value.

I used precision and recall from my confusion matricies to evaluate the effectiveness of my model.

I also did a count vectorizer to see what words were most popular in the various outcomes. The purpose of this was to see if the stopwords list could be improved with these lists.

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
