
import wikipedia
year = input("WHAT YEAR IS IT?! ")
print(year)

page = wikipedia.page(str(year))
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