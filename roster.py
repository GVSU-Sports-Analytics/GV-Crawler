from soup.soup import soup, clean_txt
import datetime


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
    def year_loop(year_links: list[str]):
        for yr in year_links:
            print(yr)
        return

    @staticmethod
    def player_loop():
        return

    def update(self):
        """
        update acts as the main function for updating
        the roster data in the database. This function
        will be run each day.
        """
        print(self.year_links)


if __name__ == "__main__":
    Roster().update()
