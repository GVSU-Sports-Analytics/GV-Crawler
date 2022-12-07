from bs4 import BeautifulSoup
import datetime
from requests import HTTPError, ConnectionError
from player import Player
import requests

ROSTER_PREFIX: str = "https://gvsulakers.com/sports/baseball/roster/"
START_URL: str = ROSTER_PREFIX + str(datetime.date.today().year)


def sewp(url: str) -> requests.request:
    try:
        return BeautifulSoup(
            requests.get(url).text,
            features="html.parser"
        )
    except HTTPError or ConnectionError as e:
        raise e(f"Problem in get request to \"{url}\"")


def get_player_divs(roster_url: str):
    html = sewp(roster_url)
    article = html.find(
        "article",
        attrs={"class": "sidearm-roster-view"}
    )

    return article.find_all(
        "div",
        attrs={"class": "sidearm-roster-player-container"}
    )


def create_players(player_divs: list[BeautifulSoup]) -> list[Player]:
    players: list[Player] = []
    for player in player_divs:
        position_div = player.find(
            "div", attrs={"class", "sidearm-roster-player-position"}
        )
        players.append(
            Player(
                _name=player.find("a", href=True).text.strip(),
                _pos=position_div.find("span").text.strip(),
                _img="",  # player.find("img", attrs={"class", "lazyloaded"})["src"],
                _height=position_div.find_all("span")[1].text.strip(),
                _weight=position_div.find_all("span")[2].text.strip(),
                _throws=position_div.find_all("span")[3].text.strip().split("/")[0],
                _hits=position_div.find_all("span")[3].text.strip().split("/")[1],
                _academic_year="",
                _previous_school=""
            )
        )
        return players


# main function
def roster():
    return


if __name__ == "__main__":
    player_divs = get_player_divs(START_URL)
    print(create_players(player_divs))
