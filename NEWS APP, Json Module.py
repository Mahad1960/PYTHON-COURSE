import requests
import json
# I have removed tesla and i had written {query} in the below "URL".
# By taking input, the information of that topic will get printed. 
print("\n")
text="WELCOME TO \"MAHAD\" NEWS CHANNEL:\n"
print(text.center(110))
query=input("Which Type Of News Are You Interested In? ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-06-17&sortBy=publishedAt&apiKey=5dc677d22c104744aadb432ce37911eb"
r=requests.get(url)
# print(r.text)             # This will print all the information of that topic.
news=json.loads(r.text)     # Converts string to "Python dic" which is stored in news.
# print(news,type(news))    # Shows the dict and its data type.
for i in news["articles"]:  # This syntax "[]" has been used because it had been converted to "dictionary".
    print(i["title"])       # "title" and "description" headings are taken from "newsapi".
    print(i["description"])
    print("---------------------------------------------------------------------------------------------------------------------")
