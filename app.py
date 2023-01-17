from flask import Flask, request, jsonify
from roster.roster import Roster
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def end_point():
    if request.is_json:
        r = json.loads(
            request.get_json()
        )
        roster = Roster(
            PREFIX=r["URL"],
        )
        roster.update()
        return jsonify(roster.RESULTS)


if __name__ == "__main__":
    app.run(
        port=3000,
        debug=True,
    )
