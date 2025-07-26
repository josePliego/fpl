import datetime

import orjson
import requests

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(url)
data = response.json()
date = datetime.datetime.now().date()
teams = data["teams"]

with open(f"data/teams/{date}.json", "wb") as f:
    f.write(
        orjson.dumps(
            teams,
            option=orjson.OPT_APPEND_NEWLINE | orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS,
        ),
    )
1