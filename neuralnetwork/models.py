import nltk
from textblob import TextBlob
import pandas as pd
import re
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


dataset = pd.read_csv('tweetslabeled.csv')
lemmatizer = WordNetLemmatizer()

corpus = []
for i in range(0, len(dataset)):
    def remove_data(vTEXT):
        vTEXT = re.sub('@[A-Za-z0–9]+', '', vTEXT)
        vTEXT = re.sub('#', '', vTEXT)  # Removing '#' hash tag
        vTEXT = re.sub('RT[\s]+', '', vTEXT)  # Removing RT
        vTEXT = re.sub('https?:\/\/\S+', '', vTEXT)  # Removing hyperlink
        vTEXT = re.sub('[^a-zA-Z]', ' ', vTEXT, flags=re.MULTILINE)
        vTEXT = vTEXT.lower()
        vTEXT = vTEXT.split()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        vTEXT = [word for word in vTEXT if not word in set(all_stopwords)]
        return vTEXT
    review = remove_data(str(dataset['body'][i]))
    review = ' '.join(review)
    corpus.append(review)
def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatize_sentence(sentence):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)
result = []
for i in range(0,len(corpus)):
    result.append(lemmatize_sentence(str(corpus[i])))
#print(result)
posts = pd.DataFrame(data=result,columns=['body'])

# Create a function to get the subjectivity
def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity

# Create a function to get the polarity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity


# Create two new columns 'Subjectivity' & 'Polarity'
posts['Subjectivity'] = posts['body'].apply(getSubjectivity)
posts['Polarity'] = posts['body'].apply(getPolarity)

def getAnalysis(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'
searchwords = {"suicide", "kill", "end my life", "never wake up", "can't go on", "not worth living", "want to die","be dead",
                   "better off without me", "tired of living", "don't want to be here", "die alone", "sleep forever"}
# creating bag of words / giving 1 or 0 for negative and positive statement which is nothing but tokenization
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(result).toarray()
y = dataset.iloc[:,-1].values

print(len(X[0]))
cv = CountVectorizer(max_features = len(X[0]))

# splitting the dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# training Navive Bayes model
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train,y_train)

# predicting the test set results
y_pred = classifier.predict(x_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(accuracy_score(y_test, y_pred))

posts['Analysis'] = posts['Polarity'].apply(getAnalysis)
posts['found'] = posts['body'].apply(lambda x: any(i in searchwords for i in x.split()))
# Show the new dataframe with columns 'Subjectivity' & 'Polarity'
posts.to_csv('filtered_post.csv')



