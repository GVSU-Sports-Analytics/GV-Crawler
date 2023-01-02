from soup.soup import soup, clean_txt
import datetime

from tqdm import tqdm
from pprint import pprint


class Roster:
    YEAR = str(datetime.datetime.today().year)
    BSBL_PREFIX = "https://gvsulakers.com"
    START_URL = BSBL_PREFIX + "/sports/baseball/roster/" + YEAR
    START_SOUP = soup(START_URL)

    @property
    def year_links(self) -> list[str]:
        """
        year_links parses through the start_soup constant
        and returns a list of roster links, one for each year
        :return: list of roster links, one for eac season
        """
        roster_select_options = self.START_SOUP.find("div", attrs={
            "class": "sidearm-roster-select"
        }).find_all("option")

        yr_links = []
        for opt in roster_select_options:
            link = self.BSBL_PREFIX + opt["value"]
            link = clean_txt(link, " ", "\n", "\t", "\r")
            yr_links.append(link)
        return yr_links

    def connect2db(self):
        return

    @staticmethod
    def player_loop(players: list):

        for player in players:
            # general info
            pos_txt = player.find("div", attrs={
                "class": "sidearm-roster-player-position"
            }).text.split()

            # some players don't have hits / throws
            if len(pos_txt) != 5:
                pos, height, weight, *_ = pos_txt
            else:
                pos, height, weight, _, hits_throws = pos_txt

            # name
            # background info
            # picture
            # add it as a row in the db

    def year_loop(self, year_links: list[str]):
        """
        year_loop will iterate through each year in the
        list of year links (property defined above), parses
        the page for player data and updates the database
        :param year_links:
        :return:
        """
        for yr in tqdm(year_links):
            html = soup(yr)
            players = html.find_all("li", attrs={
                "class": "sidearm-roster-player"
            })

            # use the year as a table name in the database
            year = "_" + yr.split("/")[-1]

            self.player_loop(players)

        return

    def update(self):
        """
        update acts as the main function for updating
        the roster data in the database. This function
        will be run each day.
        """
        self.year_loop(self.year_links)


if __name__ == "__main__":
    Roster().update()
