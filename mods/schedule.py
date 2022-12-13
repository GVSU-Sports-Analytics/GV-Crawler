"""
goal is to scrape the play by play data
for each of the games in gv baseball history
"""

from scrape import soup, get_all_tables, GVSU_PREFIX
import pandas as pd
from game import Game
from pprint import pprint
import datetime

YR = str(datetime.date.today().year)
START_URL = GVSU_PREFIX + "/sports/baseball/schedule/" + YR


def get_schedule_years() -> list[str]:
    s = soup(START_URL)
    dd = s.find("select", attrs={"id": "sidearm-schedule-select-season"})
    return [GVSU_PREFIX + v["value"] for v in dd.find_all("option")]


def box_score_links(yr_link_soup) -> (list[str], list[str]):
    # opponent images
    d = yr_link_soup.find_all(
        "div",
        attrs={"class": "sidearm-schedule-game-row"}
    )

    # find box score links
    a_s = [li.find("a", href=True) for li in yr_link_soup.find_all(
        "li",
        attrs={"class": "sidearm-schedule-game-links-boxscore"}
    )]

    images = []

    for div in d:
        try:
            images.append(GVSU_PREFIX + div.find("img")["data-src"])
        except TypeError:
            continue
    return (
        [GVSU_PREFIX + i["href"] for i in a_s],
        images
    )


def get_pbp(box_score_soup) -> dict[any, list]:
    all_pbp = box_score_soup.find(
        "div",
        attrs={"id": "inning-all"}
    )
    innings = all_pbp.find_all(
        "table",
        attrs={"class": "play-by-play"}
    )

    pbp = {}
    for i in innings:
        inn = i.find("caption").text

        rows = i.find_all("tr")
        pbp[inn] = []

        for r in rows:
            try:
                pbp[inn].append(r.find("td").text)
            except AttributeError:
                continue
    return pbp


def get_info(box_score_soup) -> dict[str, str]:
    info_panel = box_score_soup.find(
        "div",
        attrs={"class": "panel"}
    )
    return dict(
        zip(
            # each dt is like a column name and each dd is like its data point
            [d.text for d in info_panel.find_all("dt")],
            [d.text for d in info_panel.find_all("dd")]
        )
    )


def box_score_summary(soup_string) -> dict[str, pd.DataFrame]:
    """
    parses through the beautiful soup and finds the tables, returns a dictionary
    with what each table is as the key and a dataframe or list of dataframes as values
    :param soup_string: a bs4 BeautifulSoup object that has been converted to a stirng
    :return: tbl[0] is the box score,
    """
    tbls = get_all_tables(soup_string)
    return {
        "Box Score": tbls[0],
        "Scoring Summary": tbls[1],
        "Away Team Pitching": tbls[4],
        "Home Team Pitching": tbls[5],
        "pbp": tbls[6: -2],
        "Away Individual": tbls[-2],
        "Home Individual": tbls[-1]
    }


# main function of this module
def schedule() -> list[Game]:
    yrs = get_schedule_years()
    games = []

    for yr in yrs:
        yr_sewp = soup(yr)

        # think that we may want to get images from the bo
        # x score soup itself, so we can match them with the data

        bs, imgs = box_score_links(yr_sewp)

        games = []
        for b in bs:
            bs_soup = soup(b)
            info = get_info(bs_soup)
            tables = box_score_summary(str(bs_soup))
            games.append(
                Game(
                    tables=tables,
                    info=info
                )
            )
            print(games)
    return games


if __name__ == "__main__":
    schedule()
