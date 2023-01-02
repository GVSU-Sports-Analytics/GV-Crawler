from roster.roster import BaseballRoster


def main():
    return [
        BaseballRoster(
            "https://gvsulakers.com",
            "sqlite"
        ),
        BaseballRoster(
            "https://dupanthers.com",
            "sqlite"
        )
    ]


def update(*args: BaseballRoster):
    for roster in args:
        roster.update()


if __name__ == "__main__":
    update(
        *main()
    )
