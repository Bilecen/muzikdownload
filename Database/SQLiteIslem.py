import sqlite3 as sql
from Entity.GenericEntity import MuzikEntity, VideoEntity

from Kural.Sorgular import anaIslem
vt = sql.connect('islem.sqlite')
im = vt.cursor()


def MuziktabloOlustur():
    tabloolustur = """CREATE TABLE Muzikler (id integer primary key  AUTOINCREMENT ,isim TEXT, url TEXT)"""
    im.execute(tabloolustur)
    vt.commit()


def VideoTabloOlustur():
    tabloolustur = "CREATE TABLE Videolar (id INTEGER  PRIMARY  KEY  AUTOINCREMENT , isim TEXT , url TEXT ,dosya BLOB)"
    im.execute(tabloolustur)
    vt.commit()


def VideoConvertToMuzikTabloOlustur():
    tabloolustur = "CREATE TABLE VideoConvertMuzik (id INTEGER PRIMARY KEY AUTOINCREMENT ,videoid INTEGER, muzikismi TEXT,muzikboyut REAL ,olusturmatarihi datetime)"
    indexle = "CREATE UNIQUE INDEX idx_converttomuzik ON VideoConvertMuzik (videoid,muzikismi);"
    im.execute(tabloolustur)
    im.execute(indexle)
    vt.commit()


def MuzikTabloVeriEkle(isim, url):
    try:
        degerGir = "INSERT INTO Muzikler (isim , url) values (?,?);"
        im.execute(degerGir, (isim, url))
        vt.commit()
    except Exception as e:
        print(e)


def MuzikTabloVeriler():
    try:
        sorgu = "SELECT * FROM Muzikler"
        im.execute(sorgu)
        veriler = im.fetchall()
        data = []
        for v in veriler:
            m = MuzikEntity(v[0], v[1], v[2])
            data.append(m)
        return data
    except Exception as e:
        print(e)


def videoCreatedIndex():
    im.execute("CREATE UNIQUE INDEX idx_video_ismi ON Videolar (isim);")
    vt.commit()


def VideoTabloVeriEkle(isim, url, dosya):
    try:
        degergir = "INSERT INTO Videolar (isim, url, dosya) values (?,?,?);"
        im.execute(degergir, (isim, url, dosya))
        vt.commit()
    except Exception as e:
        print(e)


def VideoTabloVeriler():
    try:
        sorgu = "SELECT * FROM Videolar"
        im.execute(sorgu)
        veriler = im.fetchall()
        data = []
        for v in veriler:
            m = VideoEntity(v[0], v[1], v[2], v[3])
            data.append(m)
        return data
    except Exception as e:
        print(e)


def VideoTabloVeriSec(isim):
    try:
        sorgu = "SELECT * FROM Videolar WHERE isim=?"
        im.execute(sorgu, (isim))
        islem = im.fetchone()
        m = VideoEntity(islem[0], islem[1], islem[2], islem[3])
        return m
    except Exception as e:
        print(e)


def MuzikTabloVeriSil(id):
    try:
        sorgu = "DELETE FROM Muzikler where id={}".format(id)
        im.execute(sorgu)
        vt.commit()
        return True
    except Exception as e:
        print(e)
        return False


def VideoTabloVeriSil(id):
    try:
        sorgu = "DELETE FROM Videolar where id=?"
        im.execute(sorgu, (id))
        vt.commit()
        return True
    except Exception as e:
        print(e)
        return False


def VideoConvertToMuzikVeriEkle(videoid, muzikismi, olusturmatarihi, muzikboyut):
    try:
        insertveri = "INSERT INTO VideoConvertMuzik (videoid, muzikismi, muzikboyut, olusturmatarihi) VALUES ({},'{}',{},{})".format(
            videoid, muzikismi, muzikboyut, olusturmatarihi)
        im.execute(insertveri)
        vt.commit()
        return True
    except Exception as e:
        print(e)
        return False


def SQLControl():
    try:
        ssqlsorgu = "Select type,tbl_name From sqlite_master where type='table'"
        im.execute(ssqlsorgu)
        data = im.fetchall()
        print(data)
        return data
    except Exception as e:
        print(e)


def baglanti_kapat():
    try:
        vt.close()
        return True
    except Exception as e:
        print(e)
        return False
