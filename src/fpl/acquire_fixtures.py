import datetime

import orjson
import requests

url = "https://fantasy.premierleague.com/api/fixtures/"
response = requests.get(url)
data = response.json()
date = datetime.datetime.now().date()


with open(f"data/fixtures/{date}.json", "wb") as f:
    f.write(
        orjson.dumps(
            data,
            option=orjson.OPT_APPEND_NEWLINE | orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS,
        ),
    )
