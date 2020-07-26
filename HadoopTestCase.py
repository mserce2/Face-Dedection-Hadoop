"""
testcase yazmanın ilk koşulu gerekli kütüphaneyi eklemek bu yüzden 2 yolumuz var
1.Seçenek unittset=>> class(unittest.Testcase)
2.seçenek pyset
Ve bir diğer önemli husus fonksiyon adlarımızq test ifadesi ile başlamalıyız aksi takdirde hatalar ile karşılaşabiliriz
Sonra ki aşama olarak neyi test edeceğimizi belirlemeliyiz.Örneğin bir dizi içinde ki sayıların toplamını test ediyorsak
[1,2,3] self.assertEqual sorgusunu kullanırız.Testcase yazarken en önemli husus hangi sorgu ifadesini nerde yazacağımız
"""

import unittest
from hdfs import InsecureClient
class FileTestCase(unittest.TestCase):
    def test_file(self):
        client_hdfs = InsecureClient('http://127.0.0.1'+':50070')
        self.assertTrue(client_hdfs.download("/user/maria_dev/dataset1", ""))
        

if __name__ == '__main__':
  test_cases = [FileTestCase,]