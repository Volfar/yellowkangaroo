import os
import re
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from malware.settings import USER_AGENT
from malware.spiders.sneaky import SneakySpider

headers = {
    "User-Agent": USER_AGENT
}

def twitter_hashtag_search(hashtag):
    """ Search tweets by hashtag

    Args:
        hashtag (str)
    Return:
        list of strings
    """
    twitter = requests.get("https://twitter.com/hashtag/{0}?f=tweets&vertical=default&src=tyah&lang=en".format(hashtag), headers=headers)
    soup = BeautifulSoup(twitter.content, 'html.parser')
    return [ i.text for i in soup.findAll("div", {"class" : "js-tweet-text-container"}) ]

def text_parser(string):
    """Extract urls from string with regural expressions

    Args:
        string: input string (str)
    """
    case_1 = re.findall(r"hxxp\S+",string)
    if case_1:
        for i in case_1:
            backlog.append("http{0}".format(i[4:].replace("[.]",".")))
    case_2 = re.findall(r"\S+\[\.\]\S+",string)
    if case_2:
        for i in case_2:
            if i not in case_1 and "@" not in i:
                backlog.append(i.replace("[.]","."))
    
    pastebin_urls = re.findall(r"\S+pastebin.com\S+", string)
    if pastebin_urls:
        for url in pastebin_urls:
            url = url.split("/")
            if "raw" not in url:
                url[-1] = "raw/{0}".format(url[-1])
            url = "/".join(url)
            pastebin.append(url)


if __name__ == "__main__":
    pastebin = list()
    backlog = list()

    tweets = twitter_hashtag_search("opendir")
    for tweet in tweets:
        text_parser(tweet)

    for i in pastebin:
        r = requests.get(i)
        for j in r.text.split("\n"):
            urls = re.findall(r"https?\S+",j.strip())
            if urls:
                for url in urls:
                    backlog.append(url)

    for url in range(len(backlog)):
        validator = urlparse(backlog[url])
        if not validator.scheme:
            backlog[url]= "http://{0}".format(backlog[url])
    print("Extracted urls:")
    print("\n".join(backlog))
    process = CrawlerProcess(get_project_settings())
    SneakySpider.start_urls = backlog
    process.crawl(SneakySpider)
    process.start()