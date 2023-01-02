from soup.soup import soup, clean_txt
import datetime

YEAR = str(datetime.datetime.today().year)

BSBL_PREFIX = "https://gvsulakers.com"

START_URL = BSBL_PREFIX + "/sports/baseball/roster/" + YEAR

START_SOUP = soup(START_URL)


def year_links() -> list[str]:

    roster_select_options = START_SOUP.find("div", attrs={
        "class": "sidearm-roster-select"
        }).find_all("option")

    yr_links = []
    for opt in roster_select_options:
        link = BSBL_PREFIX + opt["value"]
        link = clean_txt(link, " ", "\n", "\t", "\r")
        yr_links.append(link)

    return yr_links


if __name__ == "__main__":
    print(year_links())
