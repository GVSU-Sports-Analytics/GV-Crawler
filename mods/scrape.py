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


def flat(l: list) -> list:
    f = []
    for sub in l:
        for i in sub:
            f.append(i)
    return f


def drop_duplicates(l: list) -> list:
    return [*set(l)]
