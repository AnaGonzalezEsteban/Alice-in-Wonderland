# 1 - OPENING THE BOOOK FILE

with open('Alice in Wonderland.txt',encoding="utf8") as Alice:
    book = list(linea.rstrip() for linea in Alice)

# 2 - TOKENIZING THE BOOK FILE WITH NLTK 

# Importing NLTK and other utilities:
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# 'book' is a list of sentences, so we need to create a function to tokenize each sentence in a list of words and concatenate all the lists in 'book':
def tokenizer(book):
    """ INPUT: a list of sentences
        OUTPUT: a list of all the words in the book without puctuation, numbers and stopwords"""
    stopWords = set(stopwords.words('english'))
    new_book = []
    for sentence in book:
        # Creating a tokenizer
        tokenizer = RegexpTokenizer(r'[a-zA-Z_]+') # to remove punctuation and numbers
        sentence = tokenizer.tokenize(sentence) # sentence = list of words
        # Lowering every word and creating a filter for stopwords 
        filteredSentence = []
        for word in sentence:
            word = word.lower()
            if word not in stopWords:
                filteredSentence.append(word) # removing stopwords
        # concatenating all the sentences in the book
        new_book += filteredSentence 
    return new_book

book = tokenizer(book)

# 3 - ABSOLUT FREQUENCY OF EACH WORD

from nltk import FreqDist

# Creating a function to get a list of the words and their frequencies

def wordsFreq(list_of_words):
    """ INPUT: a list of words
        OUTPUT: a dictionary with each word and its frequency"""
    frequency=FreqDist(list_of_words)
    # print(frequency) # <FreqDist with 3024 samples and 17126 outcomes> -- > len(w) = 3024 = number of different words,  total words in the book = 17126
    words = []
    for book in frequency.most_common(): 
        word = book
        words.append(word)
        # now words is a list of tuples. Each tuple contains a word and its frequency
    return dict(words)

w = wordsFreq(book) # dictionary with each word and its frequency