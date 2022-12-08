from requests import request, get, HTTPError, ConnectionError
from bs4 import BeautifulSoup


def soup(url: str) -> request:
    try:
        return BeautifulSoup(
            get(url).text,
            features="html.parser"
        )
    except HTTPError or ConnectionError as e:
        raise e(f"Problem in get request to \"{url}\"")


def clean(s: str) -> str:
    return s. \
        replace("\n", ""). \
        replace("\t", ""). \
        replace("\r", ""). \
        replace(" ", "")
