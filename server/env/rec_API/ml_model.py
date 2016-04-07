
from rec_app.models import Website, Category
import SiteText
import nltk
from nltk import *


# def find_features(document,word_features):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)
#
#     return features

def train():

    categories = []

    # web = Website.objects.get(url="http://www.lynnskitchenadventures.com/2009/04/homemade-enchilada-sauce.html")
    # dictionary = {}
    #
    # all_words = word_tokenize(web.body)
    # all_words = nltk.FreqDist(all_words)
    #
    # for c in web.categories.all():
    #     if c.name not in categories:
    #         print c.name
    #         categories.append(c.name)
    #         dictionary[c.name]=all_words.most_common(30)

    dictionary = {}
    categories = Category.objects.all()
    for c in categories:
        dictionary[c.name]=[]

    print dictionary

    websites = Website.objects.all()


    for web in websites:
        all_words = word_tokenize(web.body)
        all_words = nltk.FreqDist(all_words)
        word_features = list(all_words.keys())[:1]

        for c in web.categories.all():
            dictionary[c.name]=list(set(word_features).union(dictionary[c.name]))




    print
    print dictionary['recreation']





#featuresets = [(SiteText.find_features(rev), category) for (rev, category) in documents]