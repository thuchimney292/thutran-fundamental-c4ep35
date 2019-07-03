import requests
import bs4
from xlwt import Workbook
wb=Workbook()
sheet=wb.add_sheet('1')
response = requests.get('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn')
soup=bs4.BeautifulSoup(response.content.decode(),'html.parser')
#
def remove_(s):
    ls=list(s)
    i=0
    while True:
        if not (ls[i].isalpha() or ls[i].isdigit()):
            del ls[i]
        else: break
    s_new=''
    for i in range(len(ls)):
        s_new+=ls[i]
    return s_new
#print title
div= soup.find('div',id ='divTableHeader')
tr = div.table.tr
list_td= tr.find_all('td',{'class':'h_t'})
d=0
for i in list_td:
    d+=1
    sheet.write(0,d,remove_(i.string))
#print number
table=soup.find('table',id = 'tableContent')
tr_list = table.find_all("tr",{"class":'r_item'})
tr_list_a = table.find_all("tr",{"class":'r_item_a'})
for i in range(len(tr_list)):
    tr_list.insert(i*2+1,tr_list_a[i])
k=0
for i in tr_list:
    k+=1
    td= i.find_all('td',{"class":'b_r_c'})
    del td[5]
    d=0
    for j in td:
        s=j.string
        if d==0:
            s=remove_(s)
        sheet.write(k,d,s)
        d+=1
sheet.col(0).width = 12000
for i in range(4):
    sheet.col(i+1).width = 5000
wb.save('doanh_thu.xls')