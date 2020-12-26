from datetime import datetime as dt

from Database import SQLiteIslem as sql
from View import anasayfa



if __name__ == "__main__":
    anasayfa.main()
    # islemmm()
    # sql.veriTabaniCon()
    # sql.MuziktabloOlustur()
    # sql.MuzikTabloVeriEkle("deneme","deneme")

    # sql.VideoTabloOlustur()
    # sql.videoCreatedIndex()

    # sql.MuzikTabloVeriSil(1)
    # for v in sql.MuzikTabloVeriler():
    #     print(v.__str__())

    # print(sql.baglanti_kapat())
    # print(datetime.now().timestamp())
    # sql.VideoConvertToMuzikVeriEkle(1,"Deneme",datetime.now().timestamp() , 14)

