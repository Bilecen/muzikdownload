from tkinter import messagebox

from PyQt5.QtWidgets import QMessageBox

import pytube as pt
import moviepy.editor as mp
from Database.SQLiteIslem import VideoTabloVeriEkle
from zipfile import ZipFile


def videoEkle(et_videoIsmi, et_videoUrl):
    if not et_videoIsmi is "" and not et_videoUrl is "":
        print(et_videoUrl + " " + et_videoIsmi)
        try:
            yt = pt.YouTube(et_videoUrl)
            videos = yt.streams.filter(progressive=True, file_extension='mp4').first()
            # islem = videos.download()
            islem = videos.download()
            video = mp.VideoFileClip(islem)
            video.audio.write_audiofile(et_videoIsmi + ".mp3")
            file  = open(islem,encoding="utf8")
            with open(islem, 'rb') as f:
                text = f.read()
                VideoTabloVeriEkle(et_videoIsmi, et_videoUrl, text)
                print(islem)
        except Exception as e:
            print('hata')
            print(e.__str__())



    else:
        alert = QMessageBox()
        alert.setWindowTitle("Dikkat")
        alert.setText('Lütfen Url ve İsmi doldurunuz...')
        alert.setIcon(QMessageBox.Warning)
        alert.setDefaultButton(QMessageBox.Ok)
        alert.show()
        alert.exec_()


def videolariMPCevir():
    pass


def gecmisVideolariGoster():
    pass


def gecmisMuzikleriGoster():
    pass


def listeyiTemizle(lbist):
    pass


def listeyiIndir(lbist):
    pass

#
# try:
#     yt = pt.YouTube(et_videoUrl)
#     videos = yt.streams.first()
#     islem = videos.download()
#     video = mp.VideoFileClip(islem)
#     video.audio.write_audiofile(et_videoIsmi + ".mp3")
#     # file  = open(islem,encoding="utf8")
#     with open(islem, 'rb') as f:
#         text = f.read()
#         VideoTabloVeriEkle(et_videoIsmi, et_videoUrl, text)
#     print(islem)
# except Exception as e:
#     print(e)