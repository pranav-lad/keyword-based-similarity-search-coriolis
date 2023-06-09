import math
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('reuters')
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.corpus import reuters
import streamlit as st

st.title("Information Retrieval System")
# query = st.text_input("Enter your query:")
query = "This is the first document."
# Step 1: Collect the corpus
# corpus = reuters.fileids()
# corpus = [reuters.fileid for fileid in corpus]
# st.write(corpus)

# # Step 1: Collect the corpus
# corpus = ['This is the first document.',
#           'First document is good.',
#           'for the best document refer the first',
#           'THIS IS THE FIRST DOCUMENT',
#           'This is the second document.',
#           'And this is the third one.',
#           'Is this the first document?']



# Step 2: Preprocess the documents
def preprocess(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())
    
    # Remove stop words and punctuation
    words = [word for word in words if word.isalnum() and not word in stopwords.words('english')]
    
    # Stem the words
    stemmer = nltk.stem.PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    
    return words
corpus = []
for file_id in reuters.fileids():
    document = reuters.raw(str(file_id))
    corpus.append(preprocess(document))
# corpus = [preprocess(text) for text in corpus]

# Step 3: Calculate term frequencies
def calculate_tf(document):
    tf = defaultdict(int)
    for word in document:
        tf[word] += 1
    return tf

tf_corpus = [calculate_tf(document) for document in corpus]

# Step 4: Calculate inverse document frequency (IDF)
def calculate_idf(corpus):
    N = len(corpus)
    idf = defaultdict(float)
    for document in corpus:
        for word in document:
            idf[word] += 1
    
    for word in idf:
        idf[word] = math.log(N / idf[word])
    
    return idf

idf = calculate_idf(corpus)

# Step 5: Calculate document length
def calculate_document_length(document):
    length = 0
    for word in document:
        length += tf_corpus[corpus.index(document)][word] * idf[word] ** 2
    return math.sqrt(length)


# Step 8: Rank the results
# query = "This is the first document."
results = perform_query(query, idf)
# st.write(results, corpus) 
for document, score in results:
    st.write("Document:", document)
    st.write("Score:", score)
    st.write(corpus[document])
    st.write('result generated')
