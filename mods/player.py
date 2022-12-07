from collections import namedtuple

Player: namedtuple = namedtuple(
    "Player", [
        "name",
        "hits",
        "throws",
        "academic_year",
        "height",
        "weight",
        "home_town",
        "previous_school",
        "image"
    ]
)
