import cv2
import numpy as np
from PIL import Image
import os
import pandas as pd
import requests
from hdfs import InsecureClient

class DataSet:
    def __init__(self,bilgi):
        self.bilgi=bilgi
    def __str__(self):
        return "Bilgi{}".format(self.bilgi)
    def dataTopla(self):
        cam=cv2.VideoCapture(0)
        cam.set(3, 640) # video genişliği
        cam.set(4, 480) # video yüksekliği
        face_detector = cv2.CascadeClassifier("C:\\Users\\Mete\\Desktop\\dsb2\\haarcascade_frontalface_default.xml")
        # her kişi için sayısal bir yüz kimliği giriyoruz
        face_id = input('\n kullanıcı id numarası giriniz <return> ==>  ')
        print("\n [Bilgi] Yüz yakalama başlıyor.Resim kapasitesi dolana kadar bekleyin ...")
        # toplam için yüz sayısı
        count = 0
        while(True):
            ret, img = cam.read() #ret=True/Falsa döndürür. img=kare kara frame alır
            img = cv2.flip(img, 1) # flip işlemi aynada ki gibi ters görüntü oluşmasını önler
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #algoritma resimleri gri tonlamada tanımak ister.Griye çevirme işlemi yapıldı
            faces = face_detector.detectMultiScale(gray, 1.3, 5) #yüzleri kare içine alıp gri yaptık

            for (x,y,w,h) in faces: #yüzümüzün kere içindeki kordinat ayarları

                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)    #standart kare alma işlemi 
                count += 1
                print(count)
                # Çekilen görüntüyü veri kümeleri(dastaset) klasörüne kaydediyoruz.jpg formatında olduğuna dikkat edelim
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w]) #Örneğin, face_id = 1 değerine sahip bir kullanıcı için User.1.4.jpg
        
                cv2.imshow('image', img)
            k = cv2.waitKey(100) & 0xff # Eğer "ESC" tuşuna basarsak çıkış yapılır
            if k == 27:
                break
            elif count >= 50: # Resim sayımız 30 dan fazla olunca döngüden çıkar
                break
        
        print("\n [Bilgi] Exiting Program and cleanup stuff")
        #Tüm işlemler bittikden sonra videoyu serbest bırakma işlemleri yapılır.
        cam.release()
        # Do a bit of cleanup
        cv2.destroyAllWindows()
        
class DataAL:

    client = InsecureClient('http://127.0.0.1' + ':50070')
    client.download("/user/maria_dev/dataset1", "")
    path = 'dataset1'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    def getImagesAndLabels(path):
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        detector = cv2.CascadeClassifier("C:\\Users\\Mete\\Desktop\\dsb2\\haarcascade_frontalface_default.xml");
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        global ids
        ids = []
        
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    #print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))
    #with client_hdfs.write('/user/hdfs/wiki/helloworld.csv', encoding='utf-8') as writer:
    recognizer.write('trainer5.yml')

    #print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
    def DataTrainSayisi(self):
        a=np.unique(ids)
        print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
        print("Toplam {} adet yüz eğitilmiştir".format(len(a)))


def konum_al() -> object:
    res = requests.get('https://ipinfo.io/')  # bu webserver konum almamızı sağlıyor
    data = res.json()

    city = data['city']

    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    print("enlem : ", latitude)
    print("Boylam : ", longitude)
    print("Şehir : ", city)


class DataTrain:

    def DataWork(self):
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer5.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX
        id = 0
        names = ['None', 'mete', 'gg', 'amperen']
    
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)
        cam.set(4, 480)
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        while True:
            ret, img =cam.read()
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                    gray,
                    scaleFactor = 1.2,
                    minNeighbors = 5,
                    minSize = (int(minW), int(minH)),
                    )
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                    konum_al()
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
                
            cv2.imshow('camera',img)
            k = cv2.waitKey(10) & 0xff #Esc ile çıkma komutu
            if k == 27:
                break
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows() 






