from soup.soup import soup, clean_txt
from dataclasses import dataclass, field
import datetime


@dataclass
class Roster:
    """
    Roster -> class of methods that can scrape
    roster data for any team that has a sidearm
    roster. The update function is the "main loop"
    for all of these methods.
    """
    PREFIX: str

    # constants
    _YR_LINK_MIDDLE = "/sports/baseball/roster/"
    _YEAR: str = field(
        default_factory=lambda: str(datetime.datetime.today().year)
    )

    # results of the scrape
    _RESULTS: dict = field(default_factory=lambda: {})

    @property
    def YEAR(self):
        return self._YEAR

    @property
    def START_URL(self):
        return self.PREFIX + self._YR_LINK_MIDDLE + self.YEAR

    @property
    def START_SOUP(self):
        return soup(self.START_URL)

    @property
    def RESULTS(self):
        return self._RESULTS

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
            link = self.PREFIX + opt["value"]
            link = clean_txt(link, " ", "\n", "\t", "\r")
            yr_links.append(link)
        return yr_links

    @staticmethod
    def connect2db(db_name):
        return

    def player_loop(self, players: list, year: str):

        # this is kind of a crazy loop, think about
        # splitting up tasks in this loop into other funcs
        for player in players:
            # general info
            pos_txt = player.find("div", attrs={
                "class": "sidearm-roster-player-position"
            }).text.split()

            if len(pos_txt) == 5:
                pos, height, weight, _, hits_throws = pos_txt
            # some players don't have hits / throws
            elif len(pos_txt) == 4:
                pos, height, weight, *_ = pos_txt
                hits_throws = None
            # and some only have position and height on old rosters
            elif len(pos_txt) == 2:
                pos, height, *_ = pos_txt
                weight = None
                hits_throws = None
            else:
                pos, height, weight, hits_throws = None, None, None, None

            # name
            name_div = player.find("div", attrs={
                "class": "sidearm-roster-player-name"
            }).text.split()
            number, *_ = name_div
            name = " ".join(name_div[1:])

            # other info
            bg_div = player.find("div", attrs={
                "class": "sidearm-roster-player-class-hometown"
            }).text.split("\n")

            # picture
            try:
                img = self.PREFIX + player.find("img")["data-src"]
            except TypeError:
                img = None

            # add the players information to the results dictionary
            self._RESULTS[year][name] = {
                "pos": pos,
                "height": height,
                "weight": weight,
                "hits/throws": hits_throws,
                "number": number,
                "image": img,
            }

    def year_loop(self, year_links: list[str]):
        """
        year_loop will iterate through each year in the
        list of year links (property defined above), parses
        the page for player data and updates the database
        :param year_links:
        :return:
        """
        for yr in year_links:
            html = soup(yr)
            players = html.find_all("li", attrs={
                "class": "sidearm-roster-player"
            })

            # use the year as a table name in the database
            # each row will be a player
            year = "_" + yr.split("/")[-1]
            self._RESULTS[year] = {}
            self.player_loop(players, year)

        return

    def update(self):
        """
        update acts as the main function for updating
        the roster data in the database. This function
        will be run each day.
        """
        self.year_loop(self.year_links)
