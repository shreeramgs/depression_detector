import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()
email_regex = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'

def preprocess(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = re.sub(email_regex, '', text)
    text = text.lower()
    text = text.split()
    text = [lemmatizer.lemmatize(word) for word in text if not word in set(stopwords)]
    text = ' '.join(text)
    return text