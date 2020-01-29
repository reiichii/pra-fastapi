from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import MySQLdb
from collections import defaultdict

app = FastAPI()
db = MySQLdb.connect('mysql', 'admin', 'admin', 'test')


class Item(BaseModel):
    message_ids: List[str]
    appli_ids: List[str]


@app.post("/items/")
async def create_item(item: Item):
    a = item.appli_ids
    appli_ids = "'" + "','".join(a) + "'"
    m = item.message_ids
    message_ids = ",".join(m)

    c = db.cursor()
    c.execute(sql.format(appli_ids, message_ids))

    mp = {}
    res = {
        "event_counts": []
    }
    for h in c.fetchall():
        appli_id = h[0]
        message_id = h[1]
        amount = h[2]
        if appli_id not in mp:
            mp[appli_id] = {message_id: {"click": amount}}
        else:
            mp[appli_id][message_id] = {"click": amount}

    for appli_id, values in mp.items():
        r = {
            "appli_id": appli_id,
            "messages": []
        }

        for message_id, click in values.items():
            r["messages"].append({
                "message_id": message_id,
                "event_count": click
            })

        res["event_counts"].append(r)

    return res


sql = """
SELECT
    appli_id,
    message_id,
    SUM(amount)
FROM
    hourly_message_url_opens
WHERE
    appli_id IN ({})
    AND message_id IN ({})
GROUP BY
    appli_id, message_id
ORDER BY
    appli_id, message_id
;
"""
