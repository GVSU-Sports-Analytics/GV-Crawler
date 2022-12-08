"""
goal is to scrape the play by play data
for each of the games in gv baseball history
"""

from scrape import soup, clean, GVSU_PREFIX
from pprint import pprint
import datetime

START_URL: str = GVSU_PREFIX + "/sports/baseball/schedule/" + str(datetime.date.today().year)


def get_schedule_years():
    s = soup(START_URL)
    return [GVSU_PREFIX + v["value"] for v in s.find("select", attrs={
        "id": "sidearm-schedule-select-season"
    }).find_all("option")]


if __name__ == "__main__":
    pprint(get_schedule_years())
