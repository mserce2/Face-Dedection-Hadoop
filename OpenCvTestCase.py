import unittest
import sys


class OpenCVTest(unittest.TestCase):
    """ Simple functionality tests. """

    def test_import(self):
        """ Test that the cv2 module can be imported. """
        import cv2

    def test_video_capture(self):
        import cv2
        cap = cv2.VideoCapture(0)
        self.assertTrue(cap.isOpened())

    def test_dataTopla(self):
        import cv2
        cam = cv2.VideoCapture(0)
        self.assertTrue(cam.isOpened())
        cam.set(3, 640)  # video genişliği
        cam.set(4, 480)  # video yüksekliği
        face_detector = cv2.CascadeClassifier("C:\\Users\\Mete\\Desktop\\dsb2\\haarcascade_frontalface_default.xml")
        # her kişi için sayısal bir yüz kimliği giriyoruz
        face_id = input('\n kullanıcı id numarası giriniz <return> ==>  ')
        print("\n [Bilgi] Yüz yakalama başlıyor.Resim kapasitesi dolana kadar bekleyin ...")
        # toplam için yüz sayısı
        count = 0
        while (True):
            ret, img = cam.read()  # ret=True/Falsa döndürür. img=kare kara frame alır
            img = cv2.flip(img, 1)  # flip işlemi aynada ki gibi ters görüntü oluşmasını önler

            gray = cv2.cvtColor(img,
                                cv2.COLOR_BGR2GRAY)  # algoritma resimleri gri tonlamada tanımak ister.Griye çevirme işlemi yapıldı
            faces = face_detector.detectMultiScale(gray, 1.3, 5)  # yüzleri kare içine alıp gri yaptık

            for (x, y, w, h) in faces:  # yüzümüzün kere içindeki kordinat ayarları

                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # standart kare alma işlemi
                count += 1
                print(count)
                # Çekilen görüntüyü veri kümeleri(dastaset) klasörüne kaydediyoruz.jpg formatında olduğuna dikkat edelim
                self.assertTrue(cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h,
                                                                                        x:x + w]) )
                #cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h,
                                                                                        #x:x + w])  # Örneğin, face_id = 1 değerine sahip bir kullanıcı için User.1.4.jpg

                cv2.imshow('image', img)

            k = cv2.waitKey(100) & 0xff  # Eğer "ESC" tuşuna basarsak çıkış yapılır
            if k == 27:
                break
            elif count >= 50:  # Resim sayımız 30 dan fazla olunca döngüden çıkar
                break

        print("\n [Bilgi] Exiting Program and cleanup stuff")
        # Tüm işlemler bittikden sonra videoyu serbest bırakma işlemleri yapılır.
        cam.release()
        # Do a bit of cleanup
        cv2.destroyAllWindows()