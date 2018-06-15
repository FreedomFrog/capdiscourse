from django.db import models
from .nltk_tokenize import process_content
from django.utils import timezone
from .algo_based_sentiment import sentiment
from .vader_sentiment import process_content as vader_pc
from .spacy_based import identify_entities as id_ent


# Create your models here.


class Corpus(models.Model):
    text = models.TextField()
    pos = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    binary_sentiment = models.CharField(max_length=50, blank=True, null=True)
    binary_confidence = models.CharField(max_length=50, blank=True, null=True)
    TextBlob_sentiment_polarity = models.CharField(max_length=50, blank=True, null=True)
    TextBlob_sentiment_subjectivity = models.CharField(max_length=50, blank=True, null=True)
    vaderSentiment_neg = models.CharField(max_length=50, blank=True, null=True)
    vaderSentiment_neu = models.CharField(max_length=50, blank=True, null=True)
    vaderSentiment_pos = models.CharField(max_length=50, blank=True, null=True)
    vaderSentiment_compound = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pos:
            self.pos = str(process_content(self.text))
        if not self.binary_sentiment:
            algo_sent = sentiment(self.text)
            self.binary_sentiment = algo_sent[0]
            self.binary_confidence = algo_sent[1]
        if not self.TextBlob_sentiment_polarity:
            vader_textblob_sent = vader_pc(self.text)
            textblob_sent = vader_textblob_sent[0]
            self.TextBlob_sentiment_polarity = textblob_sent.polarity
            self.TextBlob_sentiment_subjectivity = textblob_sent.subjectivity
            self.vaderSentiment_neg = vader_textblob_sent[1]['neg']
            self.vaderSentiment_neu = vader_textblob_sent[1]['neu']
            self.vaderSentiment_pos = vader_textblob_sent[1]['pos']
            self.vaderSentiment_compound = vader_textblob_sent[1]['compound']
            dict_ent = id_ent(self.text)
            # for a_dict in dict_ent:
            #     a_record = Topic(topic=a_dict['text'], entity=a_dict['label'], user=)
            #     # a_record.texts.set(self.pk)
            #     a_record.save()
            #     a_record.texts.add(self)
        super().save(*args, **kwargs)

    # def pos_readable(self):


    class Meta:
        abstract = True
        verbose_name_plural = 'Corpus'


# class UserTextManager(models.Manager):
#     def create_usertext(self, user):
#         usertext = self.create(user=user)
#         dict_ent = id_ent(Corpus.text)
#         for a_dict in dict_ent:
#             a_record = Topic(topic=a_dict['text'], entity=a_dict['label'])
#             a_record.save()
#         print("Do I get called?")
#         return usertext

class UserText(Corpus):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='corpus', null=True, blank=True)
    def __str__(self):
        return self.text
    def id_topics(self):
        dict_ent = id_ent(self.text)
        for a_dict in dict_ent:
            a_record = Topic(topic=a_dict['text'], entity=a_dict['label'], user=self.user)
            # a_record.texts.set(self.pk)
            a_record.save()
            a_record.texts.add(self)


class TwitterText(Corpus):
    raw_tweet = models.TextField()


class Topic(models.Model):
    topic = models.CharField(max_length=30)
    entity = models.CharField(max_length=30)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    texts = models.ManyToManyField(UserText, default=None)
    def __str__(self):
        return self.topic
