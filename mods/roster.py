from bs4 import BeautifulSoup
import datetime
from scrape import soup
from player import Player
from pprint import pprint
from tqdm import tqdm

GVSU_PREFIX: str = "https://gvsulakers.com"
ROSTER_PREFIX: str = GVSU_PREFIX + "/sports/baseball/roster/"
START_URL: str = ROSTER_PREFIX + str(datetime.date.today().year)
START_SOUP: BeautifulSoup = soup(START_URL)


def roster_year_links() -> list[str]:
    select = START_SOUP.find("select", attrs={"id": "ddl_past_rosters"})
    return [GVSU_PREFIX + opt["value"] for opt in select.find_all("option")]


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
            "div", attrs={"class", "sidearm-roster-player-pertinents"}
        )

        height = position_div.find("span", attrs={"class": "sidearm-roster-player-height"}).text
        weight = position_div.find("span", attrs={"class": "sidearm-roster-player-weight"}).text
        throws, hits = position_div.find("span", attrs={"class": "sidearm-roster-player-custom1"}).text.split("/")
        name = position_div.find("div", attrs={"class": "sidearm-roster-player-name"}).text.strip().replace("\n", "")
        players.append(
            Player(
                name=name,
                hits=hits,
                throws=throws
            )
        )
        return players


# main function to get roster data
def roster():
    years = roster_year_links()
    players = []
    for year in tqdm(years):
        s = soup(year)
        pds = get_player_divs(s)
        players.append(create_players(pds))
    return players


if __name__ == "__main__":
    pprint(roster())
