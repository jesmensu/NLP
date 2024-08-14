import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

sentence = 'I love NLP!!'
words = word_tokenize(sentence)
sentence=sentence.lower()
print(words)

# remove stopwords
stop_words = stopwords.words('english')
text = "Messi is great player. However, he is yet to win a world cup"
words = word_tokenize(text)
filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)

# Stemming
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in filtered_words]
print(stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmText = [lemmatizer.lemmatize(word) for word in filtered_words]
print(lemmText)
