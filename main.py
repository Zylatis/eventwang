
import requests
import wikipedia
import random
import json
year = input("WHAT YEAR IS IT?! ")

try:
    pageid_json = json.loads(requests.get(f"https://en.wikipedia.org/w/api.php?action=query&titles=AD_{year}&format=json").content)
    pageid = list(pageid_json['query']['pages'].keys())[0]
    page = wikipedia.page(pageid=pageid)
    assert page.url == f"https://en.wikipedia.org/wiki/AD_{year}"
except:
    pageid_json = json.loads(requests.get(f"https://en.wikipedia.org/w/api.php?action=query&titles={year}&format=json").content)
    pageid = list(pageid_json['query']['pages'].keys())[0]
    page = wikipedia.page(pageid=pageid)
    assert page.url == f"https://en.wikipedia.org/wiki/{year}"

months =  ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'] 
content = page.content.split("\n")
allow = False
events = []
for el in content:
    if "==" in el and '===' not in el:
        if "events" in el.lower():
            allow = True
        else: 
            allow = False 

    else:
        if allow and "=" not in el and el != "":
            events.append(el)


print(random.choice(events))