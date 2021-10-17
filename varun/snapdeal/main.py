import bs4
import requests as req
keyword = input("Enter word to be scraped:")
keywords = ""
for word in keyword:
    if word == " ":
        keywords += "+"
    else:
        keywords += word
url = "https://www.snapdeal.com/search?keyword={}".format(keywords)
print(url)
response = req.get(url)
soup = bs4.BeautifulSoup(response.content)
element = soup.find_all('picture', {"class": "picture-elem", })
img_url = None
for i, ele in enumerate(element):
    with open('snapdeal{}.jpg'.format(i+1), 'wb') as f:
        img_url = element[i].source.attrs['srcset']
        img_url
        if(img_url is None):
            pass
        else:
            f.write(req.get(img_url).content)
