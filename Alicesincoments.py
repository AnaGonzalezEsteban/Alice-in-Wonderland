# 1- OPENING AND READING THE BOOK FILE

with open('Alice in Wonderland.txt',encoding="utf8") as Alice:
    book = list(linea.rstrip() for linea in Alice)

book1 = ' '
for element in book:
    book1 = book1 + ' ' + element

# 2- OPENING AND READING THE STOPWORDS FILE

with open('StopWords.txt') as SW:
    stopwords = list(linea.rstrip() for linea in SW)

# TOKENIZING THE TEXT

book1 = book1.split()

# STANDARDIZATION OF THE BOOK - CREATION OF A LIST OF 'CLEAN' WORDS

def remove_suffix(string,suffix):
    ''' INPUT: string, list of elements/suffix to delete
        OUTPUT: string without suffix'''
    wordlist = list(string)
    new_string = ''
    for character in wordlist:
        if character not in suffix:
            new_string += character
    return new_string

def normalize(list):
    ''' INPUT: list of words
        OUTPUT: list of lower words without number and suffixes'''
    NormalizedList = []
    for string in list:
        string = remove_suffix(string,['.',':',',',';','?','!','*','$','(',')','-'])
        string = string.lower()
        if string.isalpha():
            NormalizedList.append(string)
    return NormalizedList

StandardBook = normalize(book1)

# ELIMINATING STOP WORDS

def removeStopWords(list,stopwords):
    return [i for i in list if i not in stopwords]

CleanBook = removeStopWords(StandardBook,stopwords)

# COUNTING OF EACH WORD IN THE LIST OF WORDS

def count(list):
    result={}
    for element in list:
        if element not in result:
            result[element]=1
        else:
            result[element]+=1
    return result

wordsCount = count(CleanBook)