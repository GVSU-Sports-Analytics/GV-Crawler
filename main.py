from mods.roster import roster
from mods.schedule import schedule


def main() -> None:
    roster_data = roster()
    schedule_data = schedule()


if __name__ == '__main__':
    main()
