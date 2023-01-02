from bs4 import BeautifulSoup
from requests import get, HTTPError


def soup(url: str):
    try:
        r = get(url)
        return BeautifulSoup(
            r.text, features="lxml"
        )
    except HTTPError:
        raise f"Internet connection error when trying to scrape '{url}'"


def clean_txt(txt: str, *args):
    for b in args:
        txt.replace(b, "")
    return txt

# TODO: create function for getting random headers and proxies when scraping
