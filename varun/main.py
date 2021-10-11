import bs4, requests

# keyword = input("Enter word to be scraped:")
keyword = "toy"
keywords = ""
for word in keyword:
    if word == " ":
        keywords += "+"
    else:
        keywords += word
URL = "https://www.amazon.in/s?k={}&ref=nb_sb_noss_2".format(keywords)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}
webpage = requests.get(URL, headers=HEADERS)
# print(response.content)
soup = bs4.BeautifulSoup(webpage.content, features="html.parser")
elements = soup.find_all("img")
print(URL)
print(elements[0])
