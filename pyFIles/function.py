from youtube_dl import YoutubeDL
import os

def my_hook(d):
   if d['status'] == 'finished':
      file_tuple = os.path.split(os.path.abspath(d['filename']))
      print("Done downloading {}".format(file_tuple[1]))
   if d['status'] == 'downloading':
      p = d['_percent_str']
      p = p.replace('%','')
      self.progress.setValue(float(p))
      print(d['filename'], d['_percent_str'], d['_eta_str'])
      
ydl_opts = {
    'format': '171/140',  # choice of quality
    'extractaudio': True,        # only keep the audio
    'outtmpl': '/home/satwat/Downloads/%(title)s.%(ext)s',# print a list of the formats to stdout and exit         # name the file the ID of the video
    'noplaylist': True,          # only download single song, not playlist
    'listformats': False,
    'progress_hooks': [my_hook],
}


# ydl_opts = {
#       'format': 'bestaudio/best',
#       'extractaudio': True,
#       'audioformat': "mp3",
#       'progress_hooks': [self.my_hook],
#       'noplaylist': True
# }
# ydl_opts = {
#    'format': 'best',
#    'outtmpl': '/home/satwat/Downloads/%(title)s.%(ext)s',
#    'noplaylist': True,
#    'extract-audio': True
# }

video = "https://www.youtube.com/watch?v=SlPhMPnQ58k"
with YoutubeDL(ydl_opts) as ydl:
   info_dict = ydl.extract_info(video, download=True)
   video_url = info_dict.get("url", None)
   video_id = info_dict.get("id", None)
   video_title = info_dict.get('title', None)
   video_length = info_dict.get('duration')

# print(video_title)


# import youtube_dl


# # with youtube_dl.YoutubeDL(options) as ydl:
# #     ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
# from  requests import request
# link = request.GET.get(video)

# with YoutubeDL(ydl_opts) as ydl:
#    ydl.download(["https://www.youtube.com/watch?v="+link])