"""
goal is to scrape the play by play data
for each of the games in gv baseball history
"""

from scrape import soup, GVSU_PREFIX
from game import Game
from pprint import pprint
from tqdm import tqdm
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


def get_composite():
    return


def get_pitching(box_score_soup):

	print(box_score_soup.find("section", attrs={
		"class": "panel",
		"aria-label": "Team Individual Pitching Statistics"
		}).text)

	# for each table in the panel
	
	# find the columns

	# find the rows

	# for each row, match each td with its respictive col in a map


# main function of this module
def schedule() -> list[Game]:
    yrs = get_schedule_years()
    games = []

    for yr in yrs:
        yr_sewp = soup(yr)

		# think that we may want to get images from the bo
		# x score soup itself so we can match them with the data

        bs, imgs = box_score_links(yr_sewp)

        for b in bs:
            bs_soup = soup(b)
            pbp = get_pbp(bs_soup)
            info = get_info(bs_soup)
            get_pitching(bs_soup)

    return games


if __name__ == "__main__":
    schedule()
