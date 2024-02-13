import lxml
from bs4 import BeautifulSoup
import requests


url="https://www.amazon.in/Bluetooth-Tribit-Upgraded-Portable-Waterproof/dp/B078S4P3J9/ref=sr_1_2_sspa?crid=1MY8B9W4FYOKI&keywords=speaker&qid=1706963334&sprefix=speake%2Caps%2C217&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

headers = {
    "User-Agent":
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    "Accept-Language":
        'en-IN,en-GB;q=0.9,en;q=0.8,en-US;q=0.7'
}

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,"lxml")
print(soup.prettify())
price1 =soup.find('span', attrs={"class":'a-offscreen'})
print(price1)
price  = (price1.getText()).split("₹")[1]
print(price)

#add email functionality