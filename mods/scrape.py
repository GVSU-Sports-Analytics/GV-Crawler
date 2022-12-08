from requests import request, get, HTTPError, ConnectionError
from bs4 import BeautifulSoup
import random

GVSU_PREFIX: str = "https://gvsulakers.com"


def soup(url: str) -> request:
    try:
        return BeautifulSoup(
            get(url, headers=random.choice(headers)).text,
            features="html.parser"
        )
    except HTTPError or ConnectionError as e:
        raise e(f"Problem in get request to \"{url}\"")


headers = {
    "ChromeOs/Chrome": {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.9    7 Safari/537.36"
    },
    "Linux/FireFox": {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    },
    "MacOs/Safari": {
        "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Saf    ari/601.3.9"
    }
}


def clean(s: str) -> str:
    return s. \
        replace("\n", ""). \
        replace("\t", ""). \
        replace("\r", ""). \
        replace(" ", "")
