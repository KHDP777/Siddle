import json
import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import lxml
from proxy_auth import proxies

def get_inf(url):
    headers = {
            "Accept": "image / avif, image / webp, * / *",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0"
    }
    req = requests.get(url=url, headers=headers, proxies=proxies)
    return req.text

# url = "https://www.skiddle.com/"
#
# req = get_inf(url)
#
# with open("index.html", "w") as file:
#     file.write(req)
#
# with open("index.html") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
names = []
num_of_pages = 400
count_of_names = 0
for i in range(0, num_of_pages + 1, 7):
    sleep(random.randrange(2, 6))
    url = f"https://www.skiddle.com/api/v1/events/search/?limit=8&offset={i}&radius=5&minDate=2022-08-03T00:00:00&keyword=festival&hidecancelled=1&order=trending&showVirtualEvents=0&artistmeta=1&artistmetalimit=3&aggs=genreids,eventcode&pub_key=42f25&platform=web&collapse=uniquelistingidentifier"
    current_req = get_inf(url)
    json_date = json.loads(current_req)
    html_info = json_date["results"]
    # print(html_info)
    # print(html_info[0]["id"])
    for j in range(7):
        if html_info[j]["eventname"] not in names:
            count_of_names += 1
            names.append(html_info[j]["eventname"])
            event_type = html_info[j]["EventCode"]
            event_name = html_info[j]["eventname"]
            event_information = html_info[j]["venue"]
            event_href = html_info[j]["link"]
            event_date = html_info[j]["date"]
            all_events = {
                "Number in file": count_of_names,
                "Type of event": event_type,
                "Name of event": event_name,
                "Link of event": event_href,
                "Date of event": event_date,
                "All information": event_information
                }
            # print(all_events)
            with open(f"main.json", "a", encoding="utf-8") as file:
                json.dump(all_events, file, indent=4, ensure_ascii=False)

    print(f"Обработана {i} страница из {num_of_pages}...")
    # with open(f"data/page_{i}.json", "w") as file:
    #     json.dump(f"{html_info}", file, indent=4, ensure_ascii=False)



# print(dict(info))
    # print(html_info[0])
    # with open(f"data/index_{i}.html", "w") as file:
    #     file.write(html_info)


