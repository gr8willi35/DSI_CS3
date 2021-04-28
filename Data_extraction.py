import numpy as np
import pandas as pd
import requests
import json
import time
import copy

col_names=["Wikipedia ID", "Freebase ID", "Book Title", "Book Author", "Pub date","Genres","Summary"]
books_df = pd.DataFrame(books)

# must have summary and genre filled out
books_df = books_df.dropna(subset=['Genres','Summary'])
summaries = books_df[['Genres','Summary']]

def genre_scifi_tf(genre_string):
    lst = ['"Science Fiction"',"science fiction","Sci-Fi","sci-fi"]
    for i in lst:
        if i in genre_string:
            return True
    return False

summaries.insert(2, "scifi?",summaries["Genres"].apply(genre_scifi_tf))

summaries.to_csv("data/booksummaries/summaries&genres.csv")