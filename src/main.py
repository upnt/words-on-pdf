from nltk import FreqDist
from nltk.text import Text
from nltk.tokenize import word_tokenize
import pdftotext
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.tag import pos_tag

filename = 'target.pdf'

with open(filename, "rb") as f:
    pdf = pdftotext.PDF(f)

lem = WordNetLemmatizer()
tokens = word_tokenize(' '.join(pdf))

lem = WordNetLemmatizer()
tokens = word_tokenize(' '.join(pdf))
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []
for word, tag in pos_tag(tokens):
    if tag == 'NN':
        pos = 'n'
    elif tag.startswith('VB'):
        pos = 'v'
    else:
        continue
    lemmatized_tokens.append(lemmatizer.lemmatize(word, pos))

text = Text(lemmatized_tokens)
freq = FreqDist(text)

known_words = []
with open('known_word_dict.txt', mode='r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        known_words.append(line)

new_words = []
for word, num in freq.most_common():
    if not len(word) >= 4:
        continue
    if not word.isalpha():
        continue
    if not word.isascii():
        continue
    if not word in known_words:
        new_words.append(word)

with open('new_word_dict.txt', mode='w') as f:
    for word in new_words:
        f.write(word + '\n')
