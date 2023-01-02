from soup.soup import soup, clean_txt
import datetime

YEAR = str(datetime.datetime.today().year)

BSBL_PREFIX = "https://gvsulakers.com"

START_URL = BSBL_PREFIX + "/sports/baseball/roster/" + YEAR

START_SOUP = soup(START_URL)


class Roster:

    @staticmethod
    def year_links() -> list[str]:
        """
        year_links parses through the start_soup constant
        and returns a list of roster links, one for each year
        :return: list of roster links, one for eac season
        """

        roster_select_options = START_SOUP.find("div", attrs={
            "class": "sidearm-roster-select"
        }).find_all("option")

        yr_links = []
        for opt in roster_select_options:
            link = BSBL_PREFIX + opt["value"]
            link = clean_txt(link, " ", "\n", "\t", "\r")
            yr_links.append(link)
        return yr_links

    def connect2db(self):
        return

    def update(self):
        """
        update acts as the main function for updating
        the roster data in the database. This function
        will be run each day.
        """
        yr_links = self.year_links()
        print(yr_links)


if __name__ == "__main__":
    Roster().update()
