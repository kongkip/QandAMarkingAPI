import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.preprocessing import LabelEncoder

import re
import nltk

# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


dataset = pd.read_csv("IMDBDataset.csv")
dataset.head()

corpus = []
for i in tqdm(range(0, 8000)):
    review = re.sub("[^a-zA-z]", ' ', dataset["review"][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = " ".join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset["sentiment"].iloc[:8000].values
y
X.shape
y.shape
len(corpus)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

cm
text = "not back"

text = "Had dinner with girl friends. Menu is perfect, something for everyone. Service was awesome and Jason was very accommodating. Will be back definitely!"
review2 = re.sub("[^a-zA-z]", ' ', text)
review2 = review2.lower()
review2 = review2.split()
ps2 = PorterStemmer()
review2 = [ps2.stem(word) for word in review2 if not word in set(stopwords.words('english'))]
review2 = " ".join(review2)
corpus2.append(review2)
from sklearn.feature_extraction.text import CountVectorizer
cv2 = CountVectorizer(max_features = 1500)
X2 = cv2.fit_transform(corpus + corpus2).toarray()
my = X2[-1].reshape(1, -1)
result = classifier.predict(my)
if result == 1:
    answear = "Positive"
else:
    answear = "Negative"

print(answear)
