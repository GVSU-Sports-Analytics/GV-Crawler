from bs4 import BeautifulSoup
import datetime
from scrape import soup, flat, drop_duplicates
from player import Player
from pprint import pprint
from tqdm import tqdm

GVSU_PREFIX: str = "https://gvsulakers.com"
ROSTER_PREFIX: str = GVSU_PREFIX + "/sports/baseball/roster/"
START_URL: str = ROSTER_PREFIX + str(datetime.date.today().year)
START_SOUP: BeautifulSoup = soup(START_URL)


def roster_year_links() -> list[str]:
    select = START_SOUP.find(
        "select",
        attrs={"id": "ddl_past_rosters"}
    )
    return drop_duplicates([GVSU_PREFIX + opt["value"] for opt in select.find_all("option")])


def get_player_divs(roster_soup: BeautifulSoup) -> list[BeautifulSoup]:
    player_list = roster_soup.find(
        "ul",
        attrs={"class": "sidearm-roster-players"}
    )
    return player_list.find_all(
        "li",
        attrs={"class": "sidearm-roster-player"}
    )


def create_players(player_divs: list[BeautifulSoup]) -> list[Player]:
    players: list[Player] = []

    for player in player_divs:
        position_div = player.find(
            "div", attrs={"class", "sidearm-roster-player-pertinents"}
        )

        name = position_div.find("div", attrs={
            "class": "sidearm-roster-player-name"
        }).text.strip().replace("\n", "").replace("\t", "").replace("\r", "").replace(" ", "").strip()

        try:
            height = position_div.find("span", attrs={"class": "sidearm-roster-player-height"}).text
        except AttributeError:
            height = None
        try:
            weight = position_div.find("span", attrs={"class": "sidearm-roster-player-weight"}).text
        except AttributeError:
            weight = None, None
        try:
            throws, hits = position_div.find("span", attrs={"class": "sidearm-roster-player-custom1"}).text.split("/")
        except AttributeError:
            throws, hits = None, None
        try:
            _, _, academic_yr, hometown, previous_school, *_ = position_div.find("div", attrs={
                "class": "sidearm-roster-player-other"
            }).text.replace(" ", "").split("\n")
        except AttributeError:
            academic_yr, hometown, previous_school = None, None, None

        players.append(
            Player(
                name=name,
                hits=hits,
                throws=throws,
                height=height,
                weight=weight,
                academic_year=academic_yr,
                previous_school=hometown,
                home_town=previous_school
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
    all_players = roster()
    pprint(all_players[-1])
