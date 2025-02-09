import datetime

import orjson
import requests

url = "https://fantasy.premierleague.com/api/bootstrap-static/"
response = requests.get(url)
data = response.json()
date_time = datetime.datetime.now().replace(microsecond=0).isoformat()
data["extracted-on"] = date_time

with open(f"data/{date_time}.json", "wb") as f:
    f.write(
        orjson.dumps(
            data,
            option=orjson.OPT_APPEND_NEWLINE | orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS,
        ),
    )
