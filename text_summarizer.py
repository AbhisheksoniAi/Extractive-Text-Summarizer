import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import heapq

text = input("enter your text = ")

stop_word = set(stopwords.words("english"))
words = word_tokenize(text.lower())

freq_table = {}
for word in words:
    if word not in stop_word:
        freq_table[word] = freq_table.get(word, 0) + 1

sentences = sent_tokenize(text)

sentence_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in freq_table:
            sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_table[word]


summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)

summary = " ".join(summary_sentences)
print(summary)

print(sentence_scores)
