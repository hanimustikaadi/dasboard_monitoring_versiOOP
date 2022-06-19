import requests
from bs4 import BeautifulSoup

description = 'To get the latest earthquake in Indonesia from BMKG.go.id'


def ekstraksi_data():
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
        content= requests.get('https://www.bmkg.go.id/')
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
        return hasil
    else:
        return  None

def tampilkan_data(result):

    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return
    print('Gempa berdasarkan BMKG')
    print(f'tanggal {result["tanggal"]}')
    print(f'waktu {result["waktu"]}')
    print(f'magnitudo {result["magnitudo"]}')
    print(f'kedalaman {result["kedalaman"]}')
    print(f'koordinat : LS= {result["koordinat"]["LS"]}, BT = {result["koordinat"]["BT"]} ')
    print(f'lokasi {result["lokasi"]}')
    print(f'keterangan {result["keterangan"]}')
    print(f'dirasakan {result["dirasakan"]}')

#if __name__ == '__main__':
    #print('ini adalah package gempa terkini')