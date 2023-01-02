from roster.roster import Roster


def main():
    gvsu = Roster("https://gvsulakers.com")
    gvsu.update()


if __name__ == "__main__":
    main()
