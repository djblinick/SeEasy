from BeautifulSoup import BeautifulSoup
import urllib
import re
from nltk import word_tokenize
from nltk.corpus import stopwords



import string

def reach_site(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    text = soup.findAll(text=True)
    return text


def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

def clean(text):
    stop = stopwords.words('english')
    exclude = set(string.punctuation) | set(string.whitespace) | set(string.digits)

    text = [i for i in word_tokenize(text.lower()) if i not in stop]
    text = [i for i in text if i not in exclude]
    return text

class SiteText:
    def __init__(self, url):
        self.url=url
        text = reach_site(url)
        self.body = ' '.join(filter(visible, text)).lower()
        self.clean_body = clean(self.body)


