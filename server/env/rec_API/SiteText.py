from BeautifulSoup import BeautifulSoup
import urllib
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
import string



class SiteText:
    def __init__(self, url):
        self.url=url
        text = self.reach_site()
        self.body = ' '.join(filter(self.visible, text)).lower()
        self.clean_body = self.clean()

    def get_body(self):
        return self.body

    def get_clean_body(self):
        return self.clean_body

    def reach_site(self):
        html = urllib.urlopen(self.url).read()
        soup = BeautifulSoup(html)
        text = soup.findAll(text=True)
        return text


    def visible(self, element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('<!--.*-->', str(element)):
            return False
        return True

    def clean(self):
        stop = stopwords.words('english')
        exclude = set(string.punctuation) | set(string.whitespace) | set(string.digits)

        text = [i for i in word_tokenize(self.body.lower()) if i not in stop]
        text = [i for i in text if i not in exclude]
        return text


