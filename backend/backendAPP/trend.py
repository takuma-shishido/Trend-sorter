import requests
from bs4 import BeautifulSoup
import re
import json

def find_trend(span,lang):
    url = f"https://github.com/trending/{lang}?since={span}&spoken_language_code="

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    repositories = []

    for article in soup.find_all("article", {"class": "Box-row"}):
      if(article.find("p")): # None Check
        repositories.append(get_repository_by_selection(article,span))
    
    return repositories

def get_repository_by_selection(article, span):
    name = article.find("h2", {"class": "lh-condensed"}).find("a")["href"].strip(" /")
    url = article.find("h2", {"class": "lh-condensed"}).find("a")["href"]
    description = article.find("p").text.strip()
    lang = article.find("span", {"itemprop": "programmingLanguage"})
    if lang: lang = lang.text
    else:    lang = "Unknown"

    if (article.find("a", {"class": "Link--muted", "href": f"{url}/stargazers"}) == None):
        return {}
    star = int(article.find("a", {"class": "Link--muted", "href": f"{url}/stargazers"}).text.strip().replace(",", ""))
    if (article.find("a", {"class": "Link--muted", "href": f"{url}/forks"}) == None):
        return {}
    fork = int(article.find("a", {"class": "Link--muted", "href": f"{url}/forks"}).text.strip().replace(",", ""))
    if (article.find("span", {"class": "d-inline-block float-sm-right"}) == None):
        return {}
    star_by_span = int(article.find("span", {"class": "d-inline-block float-sm-right"}).text.strip().replace(",", "").replace(f"stars {get_query_for_span(span)}", "").replace(f"star {get_query_for_span(span)}", ""))

    return {
      "Name": name,
      "URL": "https://github.com" + url, 
      "Description": description,
      "Lang": lang,
      "Star": star,
      "StarBySpan": star_by_span,
      "Fork": fork
      }


def get_query_for_span(span):
    switcher = {
        "daily": "today",
        "weekly": "this week",
        "monthly": "this month",
        "default": "today"
    }
    return switcher.get(span, "daily")