
#! ####################################################################################################################################
#* #################################################################
#* #################################################################

#? YOUTUBE- DL DUMPYARD

#* #################################################################
#* #################################################################
#! ###################################################################################################################################

from youtube_dl import YoutubeDL
import os

#! DOWNLOAD PERCENT REDING
def my_hook(d):
   if d['status'] == 'finished':
      file_tuple = os.path.split(os.path.abspath(d['filename']))
      print("Done downloading {}".format(file_tuple[1]))
   if d['status'] == 'downloading':
      p = d['_percent_str']
      p = p.replace('%','')
      # self.progress.setValue(float(p))
      print("ye kar kr")
      print(d['filename'], d['_percent_str'], d['_eta_str'])
      
      
#! OPTION FORMAT
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



#! ####################################################################################################################################
#* #################################################################
#* #################################################################

#? LISTNER  DUMPYARD

#* #################################################################
#* #################################################################
#! ###################################################################################################################################

from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '2', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        return False  # stop listener; remove this if want more keys

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys




#! ####################################################################################################################################
#* #################################################################
#* #################################################################

#? RANDOM  DUMPYARD

#* #################################################################
#* #################################################################
#! ###################################################################################################################################



file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))





#! ####################################################################################################################################
#* #################################################################
#* #################################################################

#? Find default Downloads folder  DUMPYARD

#* #################################################################
#* #################################################################
#! ###################################################################################################################################






import os

    if os.name == 'nt':
        import ctypes
        from ctypes import windll, wintypes
        from uuid import UUID

        # ctypes GUID copied from MSDN sample code
        class GUID(ctypes.Structure):
            _fields_ = [
                ("Data1", wintypes.DWORD),
                ("Data2", wintypes.WORD),
                ("Data3", wintypes.WORD),
                ("Data4", wintypes.BYTE * 8)
            ] 

            def __init__(self, uuidstr):
                uuid = UUID(uuidstr)
                ctypes.Structure.__init__(self)
                self.Data1, self.Data2, self.Data3, \
                    self.Data4[0], self.Data4[1], rest = uuid.fields
                for i in range(2, 8):
                    self.Data4[i] = rest>>(8-i-1)*8 & 0xff

        SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
        SHGetKnownFolderPath.argtypes = [
            ctypes.POINTER(GUID), wintypes.DWORD,
            wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
        ]

        def _get_known_folder_path(uuidstr):
            pathptr = ctypes.c_wchar_p()
            guid = GUID(uuidstr)
            if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
                raise ctypes.WinError()
            return pathptr.value

        FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'

        def get_download_folder():
            return _get_known_folder_path(FOLDERID_Download)
    else:
        def get_download_folder():
            home = os.path.expanduser("~")
            return os.path.join(home, "Downloads")
        
print(fun())