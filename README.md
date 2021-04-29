# DSI Capstone 3
## Natural Language Processing Applied to Book Summaries.


For my final capstone project I am analyzing the wikipedia summaries for novels and determining if they should be categorized as "Science-Fiction" or not.

<img src="https://user-images.githubusercontent.com/25779351/116443332-28609880-a819-11eb-8c9f-a6a75a0f4341.jpg" width="260" height="344">

### Dataset

The dataset is the CMU Book Summary Dataset and the link to download is [here](http://www.cs.cmu.edu/~dbamman/booksummaries.html "CMU Book Summary Dataset").

The CMU dataset contains metadata including the author, title, genre and a body summary. My first step was to clean the data and create a column of targets for a model.  I am only interested in the genre and body because I want to focus on the contents of the summary to make a prediction, and I can use the genre data to create a new column of targets where the value is True (Sci-Fi) or False (not Sci-Fi)

Once the dataframe was organized I determined the genres were split at roughly 22.5% being science fiction and 77.5% not.

![Data_proportions](https://user-images.githubusercontent.com/25779351/116435335-db78c400-a810-11eb-8fce-1703b87faa24.png)

### Model Building

Next step in the process was to build a basic model. I performed a train-test-split to seperate my data into a training set and a test set, and I chose to use the ensemble method random forest from scikit learn for my model. I chose a TF*IDF Using the default parameters I was able achieve an accuracy of 84%.

The most most important words are displayed in the following figure.

![body_scores](https://user-images.githubusercontent.com/25779351/116598461-785c5f80-a8ec-11eb-80f5-11e976039f70.png)

After looking at my most important words I decided I needed to add a stopword list and implement stemming. Stopwords removes words with no bearing on the context of the document and skew the accuracy of the model.  Words like "the", "of", "and" etc. are dumped and the model can get a better accuracy score.  Stemming is the process of getting the root of words to reduce frequency.  In the most important words figure the reader may notice variations of "human".  By getting to the root words we can get a better idea of what words have an impact.  Below you can see the effects of these changes to our most important words list.

![Final Important Words](https://user-images.githubusercontent.com/25779351/116606073-d0e42a80-a8f5-11eb-8475-7d578cb29623.png)

Looking at these new words I extended my stop list, one of the words excluded was "planet", which may seem surprising considering there exists a strong correlation.  It seemed to over power the other words and excluded way more books and removing it was an improvement. Extending the stop words was an exercise in trial an error to see what worked and what didn't.

I also tried to further improve the model with bi-grams but after a few attempts removed it as it instead reduced my overall accuracy and performance. The problem is bi-grams without implementing an extensive stopwords list increases the size of the corpus too much and the model can't decipher what is significant.

With these new adjustments I produced a Confusion Matrix and Roc Curve plot. These demonstrate the performance of the model on data that it has not been trained on, the "X_test" data from the train-test-split. The area under the Roc Curve represents the accuracy of the model and the closer to 1 the more accurate it is.  The Confusion Matrix shows how the books end up categorized allowing me to see which way I am misclassifying books. Am I excluding too many that belong, or including too many that don't?

![Confusion Matrix](https://user-images.githubusercontent.com/25779351/116619092-a39f7880-a905-11eb-9d7c-4f9fb947e95f.png)


![first_roc](https://user-images.githubusercontent.com/25779351/116618993-7ce14200-a905-11eb-9975-129b1083d457.png)


Lastly I looked to adjusting my threshold acceptance to improve the model.  When looking at the Roc Curve the Threshold value is where on the curve I am setting my acceptance, so the higher the value the more book summaries are classified as sci-fi. The default is .50 so I tried increasing it by .05 intervals comparing the results, and I use a final threshold value of 0.55.  This misclassifies more books as being science fiction than the lower threshold value, but increases the total number of predictions and in a real scenario it makes more sense to put more books in front of a user and let them choose what is important.

I used precision and recall from my confusion matricies to evaluate the effectiveness of my model.


![image](https://user-images.githubusercontent.com/25779351/116622185-e7947c80-a909-11eb-8fab-3e19338f613a.png)



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


I also did a count vectorizer to see what words were most popular in the various outcomes. The purpose of this was to see if the stopwords list could be improved with these lists.
