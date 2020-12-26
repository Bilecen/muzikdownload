

from Database import SQLiteIslem as sql

import socket


def anaIslem(func):
    def veritabani_olustur():
        data = sql.SQLControl()
        print(data)
        for d in data:
            if not "VideoConvertMuzik" in d and not "Muzikler" in d and not "Videolar" in d and not "sqlite_sequence" in d:
                sql.VideoConvertToMuzikTabloOlustur()
                sql.MuziktabloOlustur()
                sql.VideoTabloOlustur()
                sql.videoCreatedIndex()
        func()

    return veritabani_olustur()


def internetVar_mi():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
