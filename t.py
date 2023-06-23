from bs4 import BeautifulSoup
import requests

url = "https://www.facebook.com/trust.dolamo.1"

r = requests.get(url)
doc = BeautifulSoup(r.text, "html.parser")

d = str(doc.prettify())
r = d.find("$")
print(r)




# f = open("trust1.html", "w")
# f.write(d)