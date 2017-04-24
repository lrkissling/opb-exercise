from HTMLParser import HTMLParser
import json
from operator import methodcaller
import os
import re

class Article(object):
    """
    An object carrying the necessary information for a news article.

    Attributes:
        title: the title of the article
        body: the body of the article
    """
    def __init__(self, title, body):
        self.title = title
        self.body = strip_tags(body)
    def word_count(self):
        """
        Returns the word count of the article, taking into account multiple
        white spaces and newlines.
        """
        return len(self.body.split())
    def preview(self):
        """
        Returns the first sentence in the body of the article. Uses an
        Imperfect-but-good-enough regex for splitting sentences.
        """
        return re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", self.body)[0]
    def print_info(self):
        """
        Prints the article information that we are concerned about. Appends an
        OS-specific newline for ease of reading.
        """
        print "Title: " + a.title
        print "Word Count: " + str(a.word_count())
        print "Preview: " + a.preview()
        print os.linesep


class MLStripper(HTMLParser):
    """
    Class written by Eloff and Ooker at http://stackoverflow.com/a/925630
    """
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    """
    Function written by Eloff and Ooker at http://stackoverflow.com/a/925630
    """
    parser = HTMLParser()
    html = parser.unescape(html)
    s = MLStripper()
    s.feed(html)
    return s.get_data()


f = open('data.json')
data = json.load(f)
f.close()

articles = []
for item in data.values():
    articles.append(Article(item["title"], item["body"]))

articles.sort(key=methodcaller("word_count"), reverse=True)

for a in articles:
    a.print_info()
