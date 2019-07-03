from youtube_dl import YoutubeDL

#download multi youtube video
dl=YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=1PeiDEO6iJk','https://www.youtube.com/watch?v=1PeiDEO6iJk'])
 
#audio
# options = {
#     'format':'bestaudio/audio'
# }
dl=YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=aJOTlE1K90k&list=RDaJOTlE1K90k&start_radio=1'])
#search and then download the first youtube video
options = {
    'default_search':'ytsearch',
    'max_download':1,
    'format':'bestaudio/audio'
}
dl=YoutubeDL(options)
dl.download(['có điều gì sao không nói cùng anh'])