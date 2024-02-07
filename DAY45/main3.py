from bs4 import BeautifulSoup

with open("DAY45/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents,"html.parser")

# print(soup.title.string)
  
# print(soup.prettify())  

# print(soup.find_all(name='p'))

# for tag in soup.find_all(name='p'):
    # print(tag.getText())

# for tag in soup.find_all(name='a'):
    # print(tag.getText())
    # print(tag.get("href"))
    
# print(soup.find(name='h1',id='name'))

# tag = soup.find(name='h3',class_='heading')
# print(tag.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# name = soup.select_one ("#name")
# print(name)

print(soup.select(".heading"))

