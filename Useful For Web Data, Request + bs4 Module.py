import requests                 # "requests" to install it.
from bs4 import BeautifulSoup   # "bs4" to install it.
response=requests.get("https://www.google.com")  # This will get me the code of "GOOGLE".
print(response.text)
# "html.parser" tells BeautifulSoup how to read and interpret the HTML code, it's like a translator that converts HTML into a structure Python can work with.
soup=BeautifulSoup(response.text,"html.parser")
print(soup.prettify())   # The .prettify() method in BeautifulSoup returns a nicely formatted version you're working with.
for heading in soup.find_all("h2"):  # This tells BeautifulSoup to find all <h2> tags in the HTML document.
    print("heading.text")