from youtube_dl import YoutubeDL
from xlrd import *
file_location ="list_song.xls"
workbook = open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
for i in range(10):
    options={
        'default_search':'ytsearch',
        'max_download':1
    }
    dl=YoutubeDL(options)
    dl.download([sheet.cell_value(i+1,1)])