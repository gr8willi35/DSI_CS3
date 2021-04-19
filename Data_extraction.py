from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

import scipy.stats as stats
import scipy

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import requests

from bs4 import BeautifulSoup

import json
import time
import copy

col_names=["Wikipedia ID", "Freebase ID", "Book Title", "Book Author", "Pub date","Genres","Summary"]

books = pd.read_csv("data/booksummaries/booksummaries.txt", 
                              header=None,sep="\t", 
                              names=col_names)

books_df = pd.DataFrame(books)
print(books_df.iloc[0:1,5:6])