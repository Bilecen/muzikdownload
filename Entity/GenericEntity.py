class GenericEntity():
    def __init__(self, id):
        self.id = id


class MuzikListE():
    def __init__(self, videoIsmi, videoUrl):
        self.vI = videoIsmi
        self.vU = videoUrl

    def __str__(self):
        return self.vI+ " "+self.vU


class MuzikEntity(GenericEntity):
    def __init__(self, id, muzikIsmi, muzikUrl):
        GenericEntity.__init__(self, id)
        self.muzikIsmi = muzikIsmi
        self.muzikUrl = muzikUrl

    def __str__(self):
        return "Ismi :" + self.muzikIsmi + " Url :" + self.muzikUrl


class VideoEntity(GenericEntity):
    def __init__(self, id, videoIsmi, videoUrl, videoDosya):
        GenericEntity.__init__(self, id)
        self.videoUrl = videoUrl
        self.videoDosya = videoDosya
        self.videoIsmi = videoIsmi

    def __str__(self):
        return "Ismi :" + self.videoIsmi


class VideoConvertMuzik(GenericEntity):
    def __int__(self, id, videoId, muzikIsmi, muzikBoyut, muzikOlusturmaTarih):
        GenericEntity.__init__(self, id)
        self.videoId = videoId
        self.muzikIsmi = muzikIsmi
        self.muzikBoyut = muzikBoyut
        self.muzikOlusturmaTarih = muzikOlusturmaTarih
