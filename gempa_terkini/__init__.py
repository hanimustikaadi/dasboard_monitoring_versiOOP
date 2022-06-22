import requests
from bs4 import BeautifulSoup
"""
method = fungsi
Field/atribute = Variabel
Constructor = Method yang panggil pertama kali saat object di ciptakan. Gunakan untuk mendeklarasikan semua field
pada kelas ini
"""



class Bencana:
    def __init__(self, url, description):
        self.description = 'To get the latest earthquake in Indonesia from BMKG.go.id'
        self.result = description
        self.url = url

    def ekstraksi_data(self):
         pass

    def tampilkan_data(self):
         pass

    def run(self):
         self.ekstraksi_data()
         self.tampilkan_data()

class BanjirTerkini(Bencana):
    def __init__(self, url):
        super(BanjirTerkini, self).__init__(url, 'not yed implemented , but it should return last flood in Indonesia')


class GempaTerkini(Bencana):
    def __init__(self, url):
        super(GempaTerkini, self).__init__(url,'To get the latest earthquake in Indonesia from BMKG.go.id' )



    def ekstraksi_data(self):
        """
        Tanggal :15 Februari 2022,232
        Waktu : 16:51:43 WIB
        magnitudo : 3.4
        kedalaman : 10 km
        lokasi  :{LS = 0.72 LS , BT=  131.51 BT}
        Keterangan : Pusat gempa berada di laut 29 km Timur Laut Kota Sorong
        Dirasakan (Skala MMI): II Kota Sorong
        return :
        """
        try:
            content= requests.get(self.url)
        except Exception:
            return None
        if content.status_code == 200:

            soup = BeautifulSoup(content.text, 'html.parser')
            title= soup.find('title')
            result = soup.find('span', { 'class': 'waktu'})

            result = result.text.split(', ')
            waktu =  result[1]
            tanggal = result[0]

            result = soup.find('div', {'class': "col-md-6 col-xs-6 gempabumi-detail no-padding"})
            result= result.findChildren('li')

            i = 0
            for res in result:
                print(i, res)
                i = i+1

            i=0
            magnitudo = None
            kedalaman = None
            ls = None
            bt= None
            pusat= None
            dirasakan = None
            lokasi = None

            print(result)

            for res in result:
                if i == 1:
                    magnitudo = res.text
                elif i == 2:
                    kedalaman = res.text
                elif i == 3:
                    koordinat = res.text.split(' - ')
                    ls = koordinat[0]
                    bt = koordinat[1]
                elif i == 4:
                    lokasi = res.text
                elif i == 5:
                    dirasakan = res.text
                i = i + 1

            hasil = dict()
            hasil['tanggal'] = tanggal  #'15 Februari 2022'
            hasil['waktu'] = waktu #
            hasil['magnitudo'] = magnitudo
            hasil['kedalaman'] =  kedalaman
            hasil['koordinat'] = {'LS': ls, 'BT': bt}
            hasil['lokasi'] = lokasi
            hasil['keterangan'] = 'Pusat gempa berada di laut 29 km Timur Laut Kota Sorong'
            hasil['dirasakan']  = dirasakan
            self.result = hasil
        else:
            return  None

    def tampilkan_data(self):

        if self.result is None:
            print('Tidak bisa menemukan data gempa terkini')
            return
        print('Gempa berdasarkan BMKG')
        print(f'tanggal {self.result["tanggal"]}')
        print(f'waktu {self.result["waktu"]}')
        print(f'magnitudo {self.result["magnitudo"]}')
        print(f'kedalaman {self.result["kedalaman"]}')
        print(f'koordinat : LS= {self.result["koordinat"]["LS"]}, BT = {self.result["koordinat"]["BT"]} ')
        print(f'lokasi {self.result["lokasi"]}')
        print(f'keterangan {self.result["keterangan"]}')
        print(f'dirasakan {self.result["dirasakan"]}')






if __name__ == '__main__':
    gempa_di_indonesia = GempaTerkini('https://www.bmkg.go.id/')
    print('deskripsi package', gempa_di_indonesia.description)
    gempa_di_indonesia.run()
    #gempa_di_indonesia.ekstraksi_data()
    #gempa_di_indonesia.tampilkan_data()