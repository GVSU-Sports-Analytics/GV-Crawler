from bs4 import BeautifulSoup
import datetime
from scrape import soup
from player import Player

ROSTER_PREFIX: str = "https://gvsulakers.com/sports/baseball/roster/"
START_URL: str = ROSTER_PREFIX + str(datetime.date.today().year)


def get_player_divs(roster_url: str) -> list[BeautifulSoup]:
    html = soup(roster_url)
    article = html.find(
        "article",
        attrs={"class": "sidearm-roster-view"}
    )

    return article.find_all(
        "div",
        attrs={
            "class": "sidearm-roster-player-container"
        }
    )


def create_players(player_divs: list[BeautifulSoup]) -> list[Player]:
    players: list[Player] = []
    for player in player_divs:
        position_div = player.find(
            "div", attrs={"class", "sidearm-roster-player-position"}
        )
        (pos, _, height, weight, handedness) = position_div.text.strip().replace(
            " ", "").replace("\r", "").replace(
            "\t", "").replace("\n\n", "\n").split("\n")

        players.append(
            Player(
                _pos=pos,
                _height=height,
                _weight=weight,
                _throws=handedness.split("/")[0],
                _hits=handedness.split("/")[1],
                _academic_year="",
                _previous_school="",
                _name="",
                _img=""
            )
        )


# main function to get roster data
def roster():
    return


if __name__ == "__main__":
    player_divs = get_player_divs(START_URL)
    create_players(player_divs)
