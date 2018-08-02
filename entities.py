import pyodbc
from urllib import request
import json
import datetime
import time

token = "account key"



for datem in data:
    feed_id = (datem[0])
    feed_name = (datem[1])
    feed_url = (datem[2])
    content_article_id = (datem[3])
    content_creator = (datem[4])
    content_name = (datem[5])
    content_pubdate = (datem[6])
    content_link = (datem[7])
    content_id = (datem[8])

    url = "https://api.dandelion.eu/datatxt/nex/v1?url=" + content_link + "&token=" + token

    print (url)

    data_request = request.urlopen(url)

    for annotations in data_request:
        parsed = json.loads(annotations)
        parsed_annotations = parsed["annotations"]
        entity_text = parsed["text"]
        entity_text_truncated = entity_text[0:998]
        for entities in parsed_annotations:
            start = entities["start"]
            end = entities["end"]
            confidence = entities["confidence"]
            html_id = entities["id"]
            title = entities["title"]
            uri = entities["uri"]
            label = entities["label"]
            timestamp_date_now = datetime.datetime.now()
            time.sleep(1)

    
        time.sleep(1)

        print("added text achim content")
    time.sleep(1)
    yes = "yes"

    print("added yes to achim content")
    time.sleep(2)
