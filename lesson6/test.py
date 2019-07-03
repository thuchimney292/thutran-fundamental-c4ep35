#from selenium import webdriver
#from selenium.webdriver.common.keys import 
import requests
import bs4
# python -m pip install requests
response = requests.get('https://dantri.com.vn/suc-khoe.htm')
soup = bs4.BeautifulSoup(response.content.decode(), 'html.parser')
# print(soup.title)
all_div = soup.find_all("div", {"data-boxtype": 'timelineposition'})
print(len(all_div))
first = all_div[1]

result=[]
for i in all_div:
    # result.append(i.div.h2.a.string)
    #print(i.a.img.attrs['src'])
    dic={
        "title":i.div.h2.a.string,
        'img':i.a.img.attrs['src']
    }
    result.append(dic)
    #print(i.div.h2.a.string)
print(result)

print(response.content.decode())
with open('dantri.html', 'wt', encoding='utf-8') as f:
    f.write(response.content.decode())
