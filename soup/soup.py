from bs4 import BeautifulSoup
from requests import get, HTTPError


def soup(url: str):
    try:
        r = get(url)
        return BeautifulSoup(
                r.text, features="lxml"
            )
    except HTTPError as e:
        raise e(f"Internet connection error when trying to scrape '{url}'")


def clean_txt(txt: str, *args):
    for b in args:
        txt.replace(b, "")
    return txt
