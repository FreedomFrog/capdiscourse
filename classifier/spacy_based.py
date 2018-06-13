import spacy

nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
#
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)


def identify_entities(text):
    list_ent = []
    nlp_text = nlp(text)
    for an_ent in nlp_text.ents:
        list_ent.append({'text': an_ent.text, 'label': an_ent.label_})
    return list_ent