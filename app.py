from roster.roster import BaseballRoster
from flask import Flask, request, jsonify
import json

import pandas as pd
import sqlite3
import os

app = Flask(__name__)


@app.route("/", methods=["POST"])
def end_point():
    if request.is_json:
        dictionary = json.loads(
            request.get_json()
        )
        roster = BaseballRoster(
            BSBL_PREFIX=dictionary["URL"],
        )
        roster.update()
        return jsonify(roster.RESULTS)
    return 300


if __name__ == "__main__":
    r = BaseballRoster("https://gvsulakers.com")
    r.update()

    db_path = os.getcwd() + "/data/gvsac.db"
    db = sqlite3.connect(db_path)
    cur = db.cursor()

    def add_tables():
        for year in r.RESULTS:
            cur.execute(f"""CREATE TABLE baseball_{year}
                    (id INT PRIMARY KEY NOT NULL);""")

            cols = list(r.RESULTS.keys())
            for col in cols:
                cur.execute(f"ALTER TABLE baseball_{year} ADD {col} TEXT;")

    add_tables()

    # def csv2sqlite():
    #     wd = os.getcwd() + "/data/"
    #     db = sqlite3.connect("data/gvsac.db")
    #     for f in os.listdir(wd):
    #         if f.split(".")[-1] == "csv":
    #             fp = wd + f
    #             yr = fp.split("_")[-1].replace(".csv", "")
    #             df = pd.read_csv(fp)
    #             df.to_sql(
    #                 name=f"baseball_roster_{yr}", con=db, if_exists="replace")
