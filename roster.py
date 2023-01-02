from soup.soup import soup
import datetime

YEAR = str(datetime.datetime.today().year)
START_URL = "https://gvsulakers.com/sports/baseball/roster/" + YEAR


if __name__ == "__main__":
    print(START_URL)
