
import requests
import wikipedia
import json
# year = input("WHAT YEAR IS IT?! ")
# print(year)
year = 1776

# req = str(requests.get(f"https://en.wikipedia.org/wiki/{year}").content)
pageid_json = json.loads(requests.get(f"https://en.wikipedia.org/w/api.php?action=query&titles={year}&format=json").content)
pageid = list(pageid_json['query']['pages'].keys())[0]
page = wikipedia.page(pageid=pageid)
assert page.url == f"https://en.wikipedia.org/wiki/{year}"

months =  ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'] 
content = page.content.split("\n")
# print(content)
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

for ev in events:
    print(ev)