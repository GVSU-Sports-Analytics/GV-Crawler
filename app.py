from roster.roster import BaseballRoster
from flask import Flask, request, jsonify
import json

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
    app.run(
        debug=True,
        port=3000,
    )
