from mods.roster import roster
# from mods.schedule import schedule
from mods.db import connect, close_db
from pprint import pprint


def main() -> None:
    roster_data = roster()

    db, cur = connect()

    cur.execute("CREATE TABLE roster;")

    db.close()
    cur.close()


if __name__ == '__main__':
    main()
