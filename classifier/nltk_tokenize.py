import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer


# example_sentence = 'Today is the best day of the rest of my life.'
# words = word_tokenize(example_sentence)
# print(words)

# sample_text = state_union.raw("2006-GWBush.txt")
# words = word_tokenize(sample_text)

# part of speech tagging
# tokenized = word_tokenize(sample_text)

def process_content(text):
    lst_tokens = []
    tokenized = word_tokenize(text)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            lst_tokens += tagged

    except Exception as e:
        print(str(e))
    return lst_tokens



# print(words)

