#-*- coding: utf-8 -*-

import json, sys
import jubatus
from jubatus.common import Datum
headlines = {}
#keys = ["HeadLine", "DateLine", "Language", "DateId", "NewsItemId", "article", "Genre1", "Genre2"]
with open(sys.argv[1], "r") as f:
    client = jubatus.Recommender("127.0.0.1", 9199, "hoge", 0)
    feeds = json.load(f, encoding="utf-8")
    for feed in feeds:
        d = Datum()
        keys = list(feed.keys())
        headlines[feed["NewsItemId"]] = feed["HeadLine"]
        for key in keys:
            try: 
                if key == "article":
                    continue
                    d.add_string(key, " ".join(feed[key]))
                elif key == "NewsItemId":
                    article_id = feed[key].encode('utf-8')
                elif key == "HeadLine":
                    d.add_string(key, feed[key].encode('utf-8'))
                else:
                    d.add_string(key, feed[key].encode('utf-8'))
            except TypeError:
                print(key, " ".join(feed[key]))
            except AttributeError:
                print("hoge")
        client.update_row(article_id, d)
    res = client.similar_row_from_id(article_id, 10)
    client.save("jubatus_hackathon")
for r in res:
    print(r.id, r.score, headlines[r.id])
     
