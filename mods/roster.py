from bs4 import BeautifulSoup
import datetime
from scrape import soup
from player import Player

ROSTER_PREFIX: str = "https://gvsulakers.com/sports/baseball/roster/"
START_URL: str = ROSTER_PREFIX + str(datetime.date.today().year)
START_SOUP: BeautifulSoup = soup(START_URL)


def roster_year_links() -> list[str]:
    print(START_SOUP.find("select", attrs={"id": "ddl_past_rosters"}).text)


def get_player_divs(roster_soup: BeautifulSoup) -> list[BeautifulSoup]:
    article = roster_soup.find(
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
    return players


# main function to get roster data
def roster():
    pds = get_player_divs(START_SOUP)
    return create_players(pds)


if __name__ == "__main__":
    roster_year_links()
    # print(roster())
