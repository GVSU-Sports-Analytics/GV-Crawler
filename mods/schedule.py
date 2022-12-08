"""
goal is to scrape the play by play data
for each of the games in gv baseball history
"""

from scrape import soup, clean, GVSU_PREFIX
from pprint import pprint
import datetime

START_URL: str = GVSU_PREFIX + \
                 "/sports/baseball/schedule/" + \
                 str(datetime.date.today().year)


def get_schedule_years():
    s = soup(START_URL)
    opts = s.find(
        "select",
        attrs={"id": "sidearm-schedule-select-season"}
    ).find_all("option")
    return [GVSU_PREFIX + v["value"] for v in opts]


def box_score_links(yr_link_soup) -> list[str]:
    a_s = [li.find("a", href=True) for li in yr_link_soup.find_all(
        "li",
        attrs={"class": "sidearm-schedule-game-links-boxscore"}
    )]
    return [GVSU_PREFIX + i["href"] for i in a_s]


# main function of this module
def schedule():
    yrs = get_schedule_years()
    for yr in yrs:
        yr_sewp = soup(yr)
        bs = box_score_links(yr_sewp)
        pprint(bs)


if __name__ == "__main__":
    schedule()
