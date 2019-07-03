import requests
import bs4
#import xlsxwriter
#import xlrd
from xlwt import Workbook
response = requests.get("https://www.apple.com/itunes/charts/songs/")
soup=bs4.BeautifulSoup(response.content.decode(),'html.parser')
section=soup.find("section",{'class':'section chart-grid'})
ul = section.div.ul
all_li = ul.find_all("li")
wb=Workbook()
sheet=wb.add_sheet('1')
sheet.write(0,0,'STT')
sheet.write(0,1,"Song")
sheet.write(0,2,"Single")
k=0
print(len(all_li))
for i in all_li:
    k+=1
    sheet.write(k,0,k)
    sheet.write(k,1,i.h3.a.string)
    sheet.write(k,2,i.h4.a.string)
sheet.col(1).width = 15000
sheet.col(2).width=15000
wb.save('list_song.xls')
