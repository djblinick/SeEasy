from rec_app.models import *
import numpy as np
import pandas as p
#url	urlid	boilerplate	alchemy_category	alchemy_category_score	avglinksize	commonlinkratio_1	commonlinkratio_2	commonlinkratio_3	commonlinkratio_4	compression_ratio	embed_ratio	framebased	frameTagRatio	hasDomainLink	html_ratio	image_ratio	is_news	lengthyLinkDomain	linkwordscore	news_front_page	non_markup_alphanum_characters	numberOfLinks	numwords_in_url	parametrizedLinkRatio	spelling_errors_ratio
DATA_PATH = './rec_app/resources/websites.tsv'

CATEGORIES_PATH = "./rec_app/resources/clean_categories.txt"

def load_data(self,path):
    lines=[]
    with open(path, 'r') as data:
        for line in data:
            lines.append(line.lower())
    return lines


# class CatMan():
#     def create_entry(self,name):
#         c = Category(name=name)
#         c.save()
#
#     def create(self):
#         lines = load_data(CATEGORIES_PATH)
#         for line in lines:
#             self.create_entry(line)
#
#         print Website.objects.all()
#
#     def delete_all(self):
#         Category.objects.all().delete()

class TSV():
    def create_web(self,url, body):
        w = Website(url=url,body=body)
        w.save()
        return w

    def create_category(self, name):
        if name:
            c = Category(name=name)
            c.save()
            return c
        return False

    def create(self):
        print "Loading text"

        lines = list(np.array(p.read_table(DATA_PATH)))
        for line in lines:
            c=self.create_category(line[2])
            w=self.create_web(line[0],line[1])
            if c:
                c.websites.add(w)
                w.categories.add(c)
                c.save()
                w.save()

        print Website.objects.all()[0]
        print Category.objects.all()[0]

    def delete_all(self):
        Website.objects.all().delete()
        Category.objects.all().delete()


