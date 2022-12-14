from mods.roster import roster
# from mods.schedule import schedule
import datetime
import pandas as pd
import sqlite3

# note that we have to be a paid member in order
# to use python anywhere database from local machine
# and also in order to web scrape from the cloud.

YEAR: int = int(datetime.date.today().year)


def get_roster_history():
    roster_data = roster()
    d = {}
    # this loop converts the nested list containing
    # the roster data into a nested dictionary containing the same information
    for i, season in enumerate(roster_data):
        d[YEAR - i] = {}
        for player in season:
            d[YEAR - i][player.name] = {}
            for col, val in player.__dict__.items():
                d[YEAR - i][player.name][col] = val
    return [[YEAR - j, pd.DataFrame.from_dict(yr_data, orient="index")] for j, yr_data in enumerate(d.values())]


def save_roster_data(rd):
    for season in rd:
        yr, data = season
        data.to_csv(f"data/{yr}_roster.csv")


if __name__ == "__main__":
    roster_data = get_roster_history()
