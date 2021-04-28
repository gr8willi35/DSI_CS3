# DSI Capstone 3
## Natural Language Processing Applied to Book Summaries.

![scifibook]<img src="(https://user-images.githubusercontent.com/25779351/116437779-635fcd80-a813-11eb-96ad-1b314be07485.jpg)" width="100"/>



For my final capstone project I am analyzing the wikipedia summaries for novels and determining if they should be categorized as "Science-Fiction" or not.

The dataset is the CMU Book Summary Dataset and the link to download is [here](http://www.cs.cmu.edu/~dbamman/booksummaries.html "CMU Book Summary Dataset").
  

The data came with 12841 entries and my first step was to clean the data and create a column of targets for a model.  Once the dataframe was organized I determined the genres were split at roughly 22.5% being science fiction and 77.5% not.


![Data_proportions](https://user-images.githubusercontent.com/25779351/116435335-db78c400-a810-11eb-8fce-1703b87faa24.png)


Next step in the process is to build a basic model, and using sklearn I was able to get a random forest model working. I chose Random forest because I wanted to avoid overfitting, and I am able to adjust threshold values easier.

Using a train test split with the split at 75% training data I was able to get an initial accuracy of 84%.

The most most important words are displayed in the following figure.

After looking at my most important words I decided I needed to add a stopword list.

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
